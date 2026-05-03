"""
THIS FILE: Main program - where all agents work together
Simple explanation: This is the "Manager" that assigns tasks to all 4 agents
"""

from crewai import Task, Crew
from agents import librarian_agent, reader_agent, strategist_agent, writer_agent
import arxiv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================
# ARXIV SEARCH FUNCTION
# ============================================

def search_arxiv_papers(topic, max_results=5):
    """
    This function finds real research papers from ArXiv
    ArXiv is a free website where scientists upload their research papers
    """
    print(f"\n🔍 Searching ArXiv for '{topic}'...")
    
    # Create ArXiv client
    client = arxiv.Client()
    
    # Create search query
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate  # Latest papers first
    )
    
    papers = []
    for paper in client.results(search):
        papers.append({
            'title': paper.title,
            'authors': [str(author) for author in paper.authors],
            'summary': paper.summary,
            'published': paper.published,
            'pdf_url': paper.pdf_url,
            'categories': paper.categories
        })
        print(f"   ✅ Found: {paper.title[:80]}...")
    
    return papers

# ============================================
# TASK 1: FIND RESEARCH PAPERS
# ============================================

def create_search_task(topic):
    # First find real ArXiv papers
    arxiv_papers = search_arxiv_papers(topic, max_results=5)
    
    # Convert those papers to text so Librarian agent can read them
    papers_text = ""
    for i, paper in enumerate(arxiv_papers, 1):
        papers_text += f"""
        Paper {i}:
        Title: {paper['title']}
        Authors: {', '.join(paper['authors'][:3])}
        Summary: {paper['summary'][:500]}...
        Published: {paper['published']}
        Categories: {', '.join(paper['categories'])}
        ---
        """
    
    search_task = Task(
        description=f"""
        Topic: {topic}
        
        Research Papers Found from ArXiv:
        {papers_text}
        
        Your job:
        1. Review these papers
        2. Identify which papers are most relevant
        3. List each paper's title and authors
        
        If any paper is missing that you think is relevant, use the search tool.
        """,
        expected_output="List of 5-7 most relevant research papers with titles and authors",
        agent=librarian_agent
    )
    return search_task, arxiv_papers

# ============================================
# TASK 2: READ PAPERS AND CREATE SUMMARIES
# ============================================

def create_analysis_task(topic, arxiv_papers):
    papers_info = ""
    for i, paper in enumerate(arxiv_papers, 1):
        papers_info += f"""
        PAPER {i}:
        Title: {paper['title']}
        Summary: {paper['summary']}
        Authors: {', '.join(paper['authors'][:3])}
        """
    
    analysis_task = Task(
        description=f"""
        Topic: {topic}
        
        Papers to Analyze:
        {papers_info}
        
        Your job - extract this information for each paper:
        
        1. Methodology: What method was used in the paper?
        2. Key Findings: What important results were found?
        3. Dataset: What data was used for research?
        4. Limitations: What weaknesses does the paper have? (authors mentioned or you think)
        5. Future Work: What did authors suggest for future?
        
        Create a TABLE with:
        | Paper Title | Methodology | Key Findings | Limitations |
        
        This table will be used by the strategist agent.
        """,
        expected_output="""A structured table with columns:
        - Paper Title
        - Methodology  
        - Key Findings
        - Limitations
        
        Plus a 2-3 line summary for each paper.""",
        agent=reader_agent
    )
    return analysis_task

# ============================================
# TASK 3: FIND RESEARCH GAPS (MOST IMPORTANT)
# ============================================

def create_gap_task(topic, arxiv_papers):
    papers_list = "\n".join([f"- {p['title']}" for p in arxiv_papers])
    
    gap_task = Task(
        description=f"""
        Topic: {topic}
        
        Available Papers:
        {papers_list}
        
        Your job - Identify Research Gaps:
        
        1. Compare: What did the papers do?
        2. Analyze: Which area was NOT covered?
        3. Look for patterns: What types of methods were used?
        4. Find gaps: Exactly what was NOT done?
        
        Examples of Gaps:
        - Paper A used X dataset, Paper B used Y dataset, but nobody tested on Z dataset
        - Papers optimized accuracy, but nobody worked on speed/model size
        - Existing methods only work on images, not on videos
        
        Answer These Specific Questions:
        Q1: What has the most research been done on currently?
        Q2: What important problem remains unsolved?
        Q3: Could there be a new direction in the future?
        Q4: What is currently missing in the field?
        
        IMPORTANT: You must EXACTLY state who did what and what was NOT done
        """,
        expected_output="""A clear list of 3-5 Research Gaps with:
        1. Gap Description (what is missing)
        2. Why Important (why filling this gap matters)
        3. Potential Research Questions (how to fill it)
        4. Suggested Methodology (what method to use)""",
        agent=strategist_agent
    )
    return gap_task

# ============================================
# TASK 4: WRITE THESIS (FINAL OUTPUT)
# ============================================

def create_writing_task(topic):
    writing_task = Task(
        description=f"""
        Topic: {topic}
        
        Your job: Write a PROFESSIONAL LITERATURE REVIEW REPORT.
        
        The report must include:
        
        1. ABSTRACT (200 words)
           - Short summary of research area
           - What is the current state
           - What gaps exist
           - What your proposed research could be
        
        2. LITERATURE REVIEW TABLE
           | Paper | Methodology | Key Findings | Limitations |
           (Details for each paper)
        
        3. RESEARCH GAPS IDENTIFIED
           Gap 1: ...
           Gap 2: ...
           Gap 3: ...
           (Detailed explanation for each gap)
        
        4. SUGGESTED THESIS TITLE
           3-4 suggested titles that address the gaps
        
        5. FUTURE RESEARCH DIRECTIONS
           - Short term (what can be done in 3-6 months)
           - Long term (what can be done in 1-2 years)
        
        Format: Professional academic style
        Language: Clear, precise, publication-ready
        """,
        expected_output="A complete literature review report in markdown format with all 5 sections",
        agent=writer_agent,
        output_file='literature_review_report.md'
    )
    return writing_task

# ============================================
# MAIN FUNCTION: RUN EVERYTHING
# ============================================

def run_research_system(topic):
    """
    This is the main function that runs everything
    Like: A Manager assigning tasks to 4 helpers
    """
    
    print("\n" + "="*60)
    print(f"🎓 DEEPRESEARCH-AI STARTING...")
    print(f"📚 Research Topic: {topic}")
    print("="*60 + "\n")
    
    # Step 1: Find research papers
    print("📖 STEP 1: Librarian Agent - Finding Research Papers...")
    search_task, arxiv_papers = create_search_task(topic)
    
    # Step 2: Analyze papers
    print("\n📖 STEP 2: Reader Agent - Reading Papers...")
    analysis_task = create_analysis_task(topic, arxiv_papers)
    
    # Step 3: Identify gaps
    print("\n📖 STEP 3: Strategist Agent - Finding Research Gaps...")
    gap_task = create_gap_task(topic, arxiv_papers)
    
    # Step 4: Write final report
    print("\n📖 STEP 4: Writer Agent - Writing Thesis...\n")
    writing_task = create_writing_task(topic)
    
    # PUT ALL AGENTS IN ONE CREW
    research_crew = Crew(
        agents=[librarian_agent, reader_agent, strategist_agent, writer_agent],
        tasks=[search_task, analysis_task, gap_task, writing_task],
        verbose=True,
        process="sequential"
    )
    
    # RUN EVERYTHING!
    print("\n🚀 SYSTEM RUNNING... 4 Agents working together!\n")
    result = research_crew.kickoff(inputs={'topic': topic})
    
    print("\n" + "="*60)
    print("✅ RESEARCH COMPLETE! Report saved as 'literature_review_report.md'")
    print("="*60)
    
    return result

# ============================================
# PROGRAM STARTS HERE
# ============================================

if __name__ == "__main__":
    YOUR_TOPIC = "Explainable AI for medical diagnosis"
    
    # Run the program
    result = run_research_system(YOUR_TOPIC)
    
    print("\n🎉 Done! Check the 'literature_review_report.md' file!")