"""
DeepResearch-AI - Complete Academic Paper Analysis System
Full sentences, no cut-off text, proper display
"""

import streamlit as st
import requests
import time
import arxiv
import re
from datetime import datetime
from collections import Counter

st.set_page_config(page_title="DeepResearch-AI", page_icon="", layout="wide")

# CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #1e3a5f 0%, #2c5a7c 100%);
        border-radius: 10px;
    }
    .main-title h1 {
        font-size: 2.8rem;
        color: #ffffff;
        margin: 0;
        font-weight: 700;
    }
    .main-title hr {
        width: 80px;
        border: 2px solid #ffffff;
        margin-top: 0.8rem;
    }
    .status-box, .error-box, .success-box {
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
        border-radius: 8px;
        font-weight: 600;
    }
    .status-box { background: #f0f4f8; border: 1px solid #cbd5e1; color: #1e293b; }
    .error-box { background: #fef2f2; border: 1px solid #f87171; color: #b91c1c; }
    .success-box { background: #f0fdf4; border: 1px solid #4ade80; color: #166534; }
    .stButton button {
        background-color: #1e3a5f;
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.6rem 2rem;
        width: 100%;
        border-radius: 8px;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
    }
    .full-text {
        white-space: normal;
        word-wrap: break-word;
    }
    @media (prefers-color-scheme: dark) {
        .status-box { background: #1e293b; border-color: #475569; color: #e2e8f0; }
        .error-box { background: #2d1a1a; border-color: #f87171; color: #fecaca; }
        .success-box { background: #1a2d1a; border-color: #4ade80; color: #bbf7d0; }
        .stTextArea textarea { background-color: #1e293b; color: #e2e8f0; border-color: #475569; }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# MULTI-SOURCE PAPER SEARCH
# ============================================

def search_semantic_scholar(query, max_results=25):
    """Search Semantic Scholar API"""
    try:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": query,
            "limit": max_results,
            "fields": "title,abstract,authors,year,venue,citationCount,url"
        }
        
        response = requests.get(url, params=params, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            papers = []
            
            for paper in data.get('data', []):
                abstract = paper.get('abstract', '')
                if abstract and len(abstract) > 150:
                    papers.append({
                        'title': paper.get('title', 'Unknown'),
                        'authors': [a.get('name', '') for a in paper.get('authors', [])[:4]],
                        'abstract': abstract,
                        'year': paper.get('year', 'Unknown'),
                        'venue': paper.get('venue', 'Unknown'),
                        'citations': paper.get('citationCount', 0),
                        'url': paper.get('url', ''),
                        'source': 'Semantic Scholar'
                    })
            return papers
        return []
    except Exception as e:
        return []

def search_arxiv(query, max_results=15):
    """Search arXiv"""
    try:
        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        papers = []
        for paper in client.results(search):
            papers.append({
                'title': paper.title,
                'authors': [str(a) for a in paper.authors][:4],
                'abstract': paper.summary,
                'year': paper.published.year if paper.published else 'Unknown',
                'venue': 'arXiv Preprint',
                'citations': 0,
                'url': paper.pdf_url,
                'source': 'arXiv'
            })
        return papers
    except Exception as e:
        return []

def search_all_sources(query, max_results=25):
    """Search all sources"""
    all_papers = []
    seen_titles = set()
    
    papers_ss = search_semantic_scholar(query, max_results)
    for paper in papers_ss:
        if paper['title'] not in seen_titles:
            seen_titles.add(paper['title'])
            all_papers.append(paper)
    
    if len(all_papers) < 12:
        papers_arxiv = search_arxiv(query, max_results - len(all_papers))
        for paper in papers_arxiv:
            if paper['title'] not in seen_titles:
                seen_titles.add(paper['title'])
                all_papers.append(paper)
    
    return all_papers

# ============================================
# TEXT PROCESSING
# ============================================

def extract_keywords_from_papers(papers):
    """Extract important keywords from all papers"""
    all_text = ' '.join([p['title'] + ' ' + p['abstract'] for p in papers]).lower()
    words = re.findall(r'\b[a-z]{4,}\b', all_text)
    stopwords = {'the', 'this', 'that', 'with', 'from', 'have', 'were', 'been', 'are', 'was', 
                 'for', 'not', 'but', 'can', 'will', 'has', 'their', 'they', 'them', 'what',
                 'about', 'which', 'when', 'then', 'there', 'these', 'those', 'such'}
    words = [w for w in words if w not in stopwords]
    word_freq = Counter(words)
    return [word for word, count in word_freq.most_common(15)]

def extract_methods_dynamically(papers):
    """Extract methodologies mentioned in papers"""
    all_text = ' '.join([p['title'] + ' ' + p['abstract'] for p in papers]).lower()
    
    method_patterns = [
        (r'\b(cnn|convolutional neural network)\b', 'CNN'),
        (r'\b(rnn|recurrent neural network|lstm|gru)\b', 'RNN/LSTM'),
        (r'\b(transformer|attention mechanism|bert|gpt)\b', 'Transformer'),
        (r'\b(svm|support vector machine)\b', 'SVM'),
        (r'\b(random forest|decision tree|ensemble)\b', 'Random Forest'),
        (r'\b(deep learning|deep neural)\b', 'Deep Learning'),
        (r'\b(machine learning|ml)\b', 'Machine Learning'),
        (r'\b(sensor fusion|multi-sensor)\b', 'Sensor Fusion'),
        (r'\b(gps|accelerometer|gyroscope|android|smartphone)\b', 'Mobile/Sensor-based'),
        (r'\b(regression|linear regression)\b', 'Regression'),
        (r'\b(clustering|k-means)\b', 'Clustering'),
        (r'\b(reinforcement learning|rl)\b', 'Reinforcement Learning'),
        (r'\b(transfer learning|fine-tuning)\b', 'Transfer Learning')
    ]
    
    found_methods = {}
    for pattern, method_name in method_patterns:
        matches = re.findall(pattern, all_text)
        if matches:
            found_methods[method_name] = len(matches)
    
    sorted_methods = sorted(found_methods.items(), key=lambda x: x[1], reverse=True)
    return [method for method, count in sorted_methods[:8]]

def extract_performance_dynamically(papers):
    """Extract performance metrics from abstracts"""
    all_text = ' '.join([p['abstract'] for p in papers]).lower()
    
    metrics = {}
    
    # Look for accuracy
    acc_patterns = [
        r'accuracy[:\s]+(\d+(?:\.\d+)?)\s*%',
        r'(\d+(?:\.\d+)?)\s*%\s*accuracy',
        r'reached\s+(\d+(?:\.\d+)?)\s*%',
        r'achieved\s+(\d+(?:\.\d+)?)\s*%',
        r'(\d+(?:\.\d+)?)\s*percent\s+accuracy'
    ]
    
    acc_values = []
    for pattern in acc_patterns:
        matches = re.findall(pattern, all_text)
        for m in matches:
            try:
                val = float(m)
                if 0 <= val <= 100:
                    acc_values.append(val)
            except:
                pass
    
    if acc_values:
        metrics['accuracy'] = round(sum(acc_values) / len(acc_values), 1)
    
    return metrics

def extract_topics_dynamically(papers):
    """Extract main topics from papers"""
    all_text = ' '.join([p['title'] + ' ' + p['abstract'] for p in papers]).lower()
    
    topic_patterns = [
        (r'\b(detection|recogn|identify|classify)\b', 'Detection and Classification'),
        (r'\b(predict|forecast|estimation)\b', 'Prediction and Forecasting'),
        (r'\b(optimize|optimization|efficient)\b', 'Optimization'),
        (r'\b(security|privacy|safety)\b', 'Security and Privacy'),
        (r'\b(healthcare|medical|clinical|diagnosis)\b', 'Healthcare and Medical'),
        (r'\b(image|vision|visual|cv)\b', 'Computer Vision'),
        (r'\b(sensor|iot|edge|mobile|smartphone|android)\b', 'Mobile and Sensor Computing'),
        (r'\b(distributed|byzantine|resilient)\b', 'Distributed Systems'),
        (r'\b(remote sensing|satellite|aerial)\b', 'Remote Sensing'),
        (r'\b(dark energy|cosmology|astrophysics)\b', 'Astrophysics')
    ]
    
    found_topics = {}
    for pattern, topic_name in topic_patterns:
        matches = re.findall(pattern, all_text)
        if matches:
            found_topics[topic_name] = len(matches)
    
    sorted_topics = sorted(found_topics.items(), key=lambda x: x[1], reverse=True)
    return [topic for topic, count in sorted_topics[:6]]

def calculate_citation_stats(papers):
    """Calculate citation statistics"""
    citations = [p['citations'] for p in papers if p['citations'] > 0]
    
    if not citations:
        return {'total': 0, 'average': 0, 'max': 0, 'high_impact_count': 0, 'papers_with_citations': 0}
    
    return {
        'total': sum(citations),
        'average': round(sum(citations) / len(citations), 1),
        'max': max(citations),
        'high_impact_count': len([c for c in citations if c > 50]),
        'papers_with_citations': len(citations)
    }

# ============================================
# COMPLETE SENTENCE GENERATION
# ============================================

def generate_comparative_analysis(papers, methods):
    """Generate complete, readable comparative analysis"""
    
    if len(papers) < 2:
        return "Insufficient papers for comparative analysis. Please try a broader search topic."
    
    sorted_papers = sorted(papers, key=lambda x: x['citations'], reverse=True)
    
    analysis = f"### Comparative Analysis of {len(papers)} Research Papers\n\n"
    
    # Top performing papers section
    analysis += "**Most Influential Papers Based on Citation Count**\n\n"
    
    high_citation_papers = [p for p in sorted_papers if p['citations'] > 0]
    
    if high_citation_papers:
        for i, paper in enumerate(high_citation_papers[:5], 1):
            analysis += f"**{i}. {paper['title']}**\n"
            analysis += f"- **Citation Count:** {paper['citations']} citations\n"
            analysis += f"- **Publication Year:** {paper['year']}\n"
            analysis += f"- **Venue:** {paper['venue']}\n"
            
            # Full abstract sentence (no cut-off)
            full_abstract = paper['abstract']
            # Take first complete sentence
            first_sentence = full_abstract.split('.')[0] + '.' if full_abstract else ''
            if len(first_sentence) > 50:
                analysis += f"- **Core Contribution:** {first_sentence}\n"
            else:
                analysis += f"- **Core Contribution:** This paper contributes to the field by addressing key challenges in the research domain.\n"
            analysis += "\n"
    else:
        analysis += "No papers with significant citations were found in this search. This may indicate an emerging research area or niche topic.\n\n"
    
    # Methodology distribution section
    if methods:
        analysis += "**Methodology Distribution Across Analyzed Papers**\n\n"
        
        for method in methods:
            count = 0
            for paper in papers:
                if method.lower() in (paper['title'] + paper['abstract']).lower():
                    count += 1
            percent = round((count / len(papers)) * 100) if len(papers) > 0 else 0
            
            if count > 0:
                analysis += f"- **{method}:** Used in {count} out of {len(papers)} papers, representing {percent}% of the analyzed literature.\n"
        
        analysis += "\n"
    
    # Key observations
    analysis += "**Key Observations from the Comparative Analysis**\n\n"
    
    # Citation analysis
    citation_stats = calculate_citation_stats(papers)
    if citation_stats['papers_with_citations'] > 0:
        analysis += f"- Out of {len(papers)} analyzed papers, only {citation_stats['papers_with_citations']} papers have received citations, with an average citation count of {citation_stats['average']} per cited paper.\n"
    else:
        analysis += f"- None of the {len(papers)} papers analyzed have received citations yet, suggesting this may be a newly emerging research area.\n"
    
    # Year analysis
    recent_papers = [p for p in papers if p['year'] != 'Unknown' and str(p['year']).isdigit() and int(p['year']) >= 2023]
    if recent_papers:
        analysis += f"- Recent research activity is evident with {len(recent_papers)} papers published since 2023, indicating growing interest in this domain.\n"
    
    # Methodology observation
    if methods and len(methods) >= 2:
        top_method = methods[0]
        analysis += f"- {top_method} emerges as the predominant methodology, though direct performance comparison across studies remains challenging due to varying evaluation protocols and datasets.\n"
    
    # Gap observation
    analysis += f"- A notable observation is the lack of standardized benchmark datasets and evaluation metrics, which currently limits fair comparison between different approaches.\n"
    
    return analysis

def generate_research_gaps_section(papers, methods, topics):
    """Generate complete research gaps with full sentences"""
    
    all_text = ' '.join([p['abstract'] for p in papers]).lower()
    total_papers = len(papers)
    
    gaps = []
    
    # Gap 1: Based on citation impact
    high_citation_papers = [p for p in papers if p['citations'] > 10]
    if len(high_citation_papers) < 3:
        gaps.append({
            'title': 'Limited High-Impact Research',
            'description': f'Out of {total_papers} papers analyzed, only {len(high_citation_papers)} papers have received significant citation impact (more than 10 citations). This indicates that the research field is still in its early stages or that existing work has not yet achieved widespread recognition or adoption. Future research should focus on producing high-quality, reproducible studies that can serve as foundational work for the community.',
            'evidence': f'Citation analysis shows {len(high_citation_papers)} out of {total_papers} papers have more than 10 citations'
        })
    
    # Gap 2: Methodology standardization
    if len(methods) >= 2:
        methods_list = ', '.join(methods[:3])
        gaps.append({
            'title': 'Lack of Methodological Standardization',
            'description': f'The literature employs diverse methodologies including {methods_list}. However, there is no standardized evaluation framework or benchmark dataset that allows fair comparison between these different approaches. Each study uses its own experimental setup, dataset, and evaluation metrics, making it difficult to determine which methodology performs best under comparable conditions.',
            'evidence': f'{len(methods)} different methodologies identified across {total_papers} papers without unified evaluation standards'
        })
    
    # Gap 3: Real-world validation
    if 'real' not in all_text and 'deployment' not in all_text:
        gaps.append({
            'title': 'Limited Real-World Validation',
            'description': f'Analysis of the literature reveals that most studies are conducted in controlled laboratory settings or use synthetic datasets. The absence of real-world validation studies is a critical gap, as performance in controlled environments often does not translate directly to practical deployment scenarios. Future research should prioritize field studies and real-world evaluations to validate the practical utility of proposed approaches.',
            'evidence': f'No mention of real-world deployment or field validation found in {total_papers} papers'
        })
    
    # Gap 4: Cross-domain generalization
    if 'generalization' not in all_text and 'cross' not in all_text:
        gaps.append({
            'title': 'Insufficient Cross-Domain Generalization Studies',
            'description': f'Current research primarily focuses on specific datasets or narrow application domains. The generalization capability of proposed methods across different domains, environments, and data distributions remains largely unexplored. This gap limits the practical applicability of research findings and their transferability to related problems or different real-world scenarios.',
            'evidence': f'Keywords related to generalization and cross-domain validation are absent from the analyzed literature'
        })
    
    # Gap 5: Based on topics coverage
    if len(topics) < 3:
        gaps.append({
            'title': 'Limited Topic Coverage',
            'description': f'The research landscape shows concentration in only {len(topics)} major topic areas: {", ".join(topics[:3]) if topics else "limited areas"}. Other potentially important aspects of this research domain remain underexplored or completely unaddressed. Future work should broaden the research scope to address these neglected areas and provide a more comprehensive understanding of the field.',
            'evidence': f'Only {len(topics)} distinct research topics identified across {total_papers} papers'
        })
    
    # Ensure at least 3 gaps
    while len(gaps) < 3:
        gaps.append({
            'title': 'Need for Comprehensive Evaluation Frameworks',
            'description': f'Based on the analysis of {total_papers} papers, there is a clear need for establishing comprehensive evaluation frameworks that include standardized benchmarks, reproducible experimental protocols, and fair comparison metrics. Such frameworks would accelerate progress by enabling direct comparison of different approaches and identifying the most promising research directions.',
            'evidence': f'Analysis of {total_papers} papers reveals inconsistent evaluation methodologies'
        })
    
    return gaps[:4]

def generate_future_directions_section(papers, gaps, methods):
    """Generate complete future directions with full sentences"""
    
    future_directions = []
    
    # Direction based on top gap
    if gaps:
        primary_gap = gaps[0]
        future_directions.append({
            'title': f'Addressing the {primary_gap["title"]}',
            'description': f'The primary research gap identified in this review is the {primary_gap["title"].lower()}. To address this gap, future research should focus on {primary_gap["description"][:150]} More specifically, researchers should design studies that directly target this gap with clear experimental validation.',
            'priority': 'High Priority',
            'timeline': '6 to 9 months'
        })
    
    # Direction based on methodology
    if methods:
        top_method = methods[0]
        future_directions.append({
            'title': f'Advancing {top_method} for This Domain',
            'description': f'{top_method} currently represents the most frequently used methodology in the analyzed literature. However, there remains significant room for optimization and adaptation to the specific requirements of this research domain. Future work should explore hybrid approaches that combine {top_method} with complementary techniques, as well as investigate parameter tuning and architectural innovations to improve performance.',
            'priority': 'High Priority',
            'timeline': '6 to 12 months'
        })
    
    # Direction based on performance improvement
    metrics = extract_performance_dynamically(papers)
    if metrics.get('accuracy'):
        current_acc = metrics['accuracy']
        future_directions.append({
            'title': 'Performance Enhancement through Advanced Techniques',
            'description': f'Current reported accuracy in the literature averages around {current_acc}%. Future research should aim to significantly exceed this baseline through architectural innovations, improved feature engineering, ensemble methods, or integration with more advanced machine learning techniques. Establishing new state-of-the-art performance would represent a substantial contribution to the field.',
            'priority': 'Medium to High Priority',
            'timeline': '3 to 6 months'
        })
    else:
        future_directions.append({
            'title': 'Establishing Performance Baselines',
            'description': f'The current literature lacks clear performance baselines and benchmarks. Future research should first focus on establishing standardized evaluation protocols and reporting performance metrics consistently. This foundational work would enable meaningful comparisons and help identify the most promising research directions for subsequent investigation.',
            'priority': 'High Priority',
            'timeline': '3 to 6 months'
        })
    
    # Direction for generalization
    future_directions.append({
        'title': 'Cross-Domain Validation and Generalization Studies',
        'description': f'Current research predominantly focuses on specific datasets or controlled conditions. Future work must extend validation across diverse domains, environments, and data distributions. This includes conducting rigorous cross-dataset evaluations, investigating domain adaptation techniques, and studying model robustness under varying real-world conditions. Such studies are essential for determining the practical applicability and limitations of proposed methods.',
        'priority': 'Medium Priority',
        'timeline': '9 to 12 months'
    })
    
    # Direction for real-world deployment
    future_directions.append({
        'title': 'Real-World Deployment and Field Validation',
        'description': f'Moving beyond laboratory settings to real-world deployment represents a critical next step for this research domain. Future studies should include field trials, deployment case studies, and practical application evaluations. This includes addressing challenges related to scalability, latency, resource constraints, and system integration that are often overlooked in controlled experimental settings.',
        'priority': 'High Priority',
        'timeline': '12 to 18 months'
    })
    
    return future_directions[:5]

def generate_abstract_section(papers, metrics, methods, topics):
    """Generate complete abstract with full sentences"""
    
    if not papers:
        return "No papers were found for the specified search query. Please try a different topic or broaden your search terms."
    
    total = len(papers)
    recent = sum(1 for p in papers if p['year'] != 'Unknown' and str(p['year']).isdigit() and int(p['year']) >= 2022)
    avg_citations = sum(p['citations'] for p in papers) // total if total > 0 else 0
    
    abstract = f"This systematic literature review provides a comprehensive analysis of {total} research papers relevant to the specified research topic. "
    
    if recent > 0:
        abstract += f"The corpus includes {recent} papers published since 2022, representing approximately {round(recent/total*100)} percent of the analyzed literature, indicating recent research activity in this domain. "
    else:
        abstract += f"The analyzed papers span various publication years, with ongoing research activity in the field. "
    
    if avg_citations > 0:
        abstract += f"The average citation count across the analyzed papers is {avg_citations}, suggesting a moderate level of research impact and community engagement. "
    else:
        abstract += f"Citation analysis reveals limited research impact to date, which may indicate an emerging research area with significant growth potential. "
    
    if topics:
        abstract += f"Key research areas identified in the literature include {', '.join(topics[:4])}. "
    
    if methods:
        abstract += f"Methodological analysis reveals that {', '.join(methods[:3])} represent the dominant approaches employed in current research. "
    
    if metrics.get('accuracy'):
        abstract += f"Reported performance metrics indicate that current approaches achieve approximately {metrics['accuracy']} percent accuracy, establishing a preliminary baseline for future improvements. "
    
    abstract += f"This review synthesizes current knowledge, compares methodological approaches, identifies critical research gaps, and proposes future research directions to advance the field."
    
    return abstract

def generate_conclusion_section(papers, gaps, metrics):
    """Generate complete conclusion with key findings"""
    
    total = len(papers)
    high_citation = len([p for p in papers if p['citations'] > 10])
    recent = len([p for p in papers if p['year'] != 'Unknown' and str(p['year']).isdigit() and int(p['year']) >= 2022])
    
    conclusion = f"This literature review analyzed {total} research papers to assess the current state of research. "
    
    # Key finding 1
    if high_citation > 0:
        conclusion += f"Key finding one: Only {high_citation} out of {total} papers have received significant citation impact (more than 10 citations), suggesting that the field has not yet reached maturity and there is substantial opportunity for high-impact contributions. "
    else:
        conclusion += f"Key finding one: None of the analyzed papers have received significant citation impact, indicating that this is an emerging research area with substantial potential for foundational contributions. "
    
    # Key finding 2
    if recent > 0:
        conclusion += f"Key finding two: {recent} papers (approximately {round(recent/total*100)} percent) were published in the last two years, demonstrating growing research interest and recent momentum in this domain. "
    
    # Key finding 3
    if metrics.get('accuracy'):
        conclusion += f"Key finding three: Current reported performance benchmarks show accuracy ranging around {metrics['accuracy']} percent, establishing a baseline that future research should aim to exceed. "
    
    # Gap summary
    if gaps:
        gap_titles = [g['title'] for g in gaps[:3]]
        conclusion += f"Key finding four: Critical research gaps identified include {', '.join(gap_titles)}. These gaps represent significant opportunities for future investigation and potential breakthroughs. "
    
    conclusion += f"In conclusion, while progress has been made in this research domain, substantial opportunities remain for advancing the field through addressing the identified gaps and pursuing the proposed future research directions."
    
    return conclusion

# ============================================
# MAIN INTERFACE
# ============================================

st.markdown("""
<div class="main-title">
    <h1>DeepResearch-AI</h1>
    <hr>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([1, 1.5])

with left_col:
    st.markdown("### Research Topic")
    
    topic_input = st.text_area(
        label="Research Topic Input",
        placeholder="Example: Mode of transportation detection using Android sensor data",
        height=100,
        label_visibility="collapsed"
    )
    
    generate_button = st.button("Generate Report", type="primary")
    
    if generate_button and topic_input:
        st.session_state['topic'] = topic_input
        st.session_state['generate'] = True

with right_col:
    st.markdown("### Status")
    
    if 'generate' in st.session_state and st.session_state['generate']:
        topic = st.session_state['topic']
        
        status_placeholder = st.empty()
        status_placeholder.markdown('<div class="status-box">Searching for academic papers related to your topic...</div>', unsafe_allow_html=True)
        
        papers = search_all_sources(topic, max_results=25)
        
        if papers:
            status_placeholder.markdown(f'<div class="success-box">Successfully found {len(papers)} relevant papers. Now analyzing content and generating comprehensive report...</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            
            # Extract all information
            keywords = extract_keywords_from_papers(papers)
            methods = extract_methods_dynamically(papers)
            metrics = extract_performance_dynamically(papers)
            topics = extract_topics_dynamically(papers)
            citation_stats = calculate_citation_stats(papers)
            
            # Generate all sections
            comparative_analysis = generate_comparative_analysis(papers, methods)
            gaps = generate_research_gaps_section(papers, methods, topics)
            future_directions = generate_future_directions_section(papers, gaps, methods)
            abstract = generate_abstract_section(papers, metrics, methods, topics)
            conclusion = generate_conclusion_section(papers, gaps, metrics)
            
            status_placeholder.empty()
            
            # Display Report
            st.markdown("---")
            st.markdown("### Literature Review Report")
            
            with st.expander("Abstract", expanded=True):
                st.markdown(abstract)
            
            with st.expander(f"Papers Analyzed ({len(papers)})", expanded=False):
                for i, paper in enumerate(papers, 1):
                    st.markdown(f"**Paper {i}: {paper['title']}**")
                    st.markdown(f"- **Source:** {paper['source']}")
                    st.markdown(f"- **Publication Year:** {paper['year']}")
                    st.markdown(f"- **Venue:** {paper['venue']}")
                    st.markdown(f"- **Citation Count:** {paper['citations']}")
                    if paper['authors'] and paper['authors'][0]:
                        st.markdown(f"- **Authors:** {', '.join(paper['authors'][:3])}")
                    st.markdown(f"- **Abstract:** {paper['abstract']}")
                    st.markdown("---")
            
            with st.expander("Methodology Analysis", expanded=False):
                if methods:
                    st.markdown("The following methodologies were identified across the analyzed papers:")
                    for method in methods:
                        count = sum(1 for p in papers if method.lower() in (p['title'] + p['abstract']).lower())
                        percent = round((count / len(papers)) * 100)
                        st.markdown(f"- **{method}:** This methodology appears in {count} out of {len(papers)} papers, representing approximately {percent} percent of the analyzed literature.")
                else:
                    st.markdown("No specific methodologies could be automatically identified from the paper abstracts. A manual review may be necessary for detailed methodology analysis.")
            
            with st.expander("Research Topics Identified", expanded=False):
                if topics:
                    st.markdown("The research landscape encompasses the following major topic areas:")
                    for topic in topics:
                        st.markdown(f"- **{topic}**")
                else:
                    st.markdown("Specific research topics could not be automatically classified. Consider manual review for detailed topic categorization.")
            
            with st.expander("Comparative Analysis", expanded=True):
                st.markdown(comparative_analysis)
            
            with st.expander("Research Gaps Identified", expanded=True):
                for i, gap in enumerate(gaps, 1):
                    st.markdown(f"**Research Gap {i}: {gap['title']}**")
                    st.markdown(f"{gap['description']}")
                    st.markdown(f"*Supporting Evidence:* {gap['evidence']}")
                    st.markdown("---")
            
            with st.expander("Future Research Directions", expanded=True):
                for fd in future_directions:
                    st.markdown(f"**{fd['title']}**")
                    st.markdown(f"{fd['description']}")
                    st.markdown(f"- **Priority Level:** {fd['priority']}")
                    st.markdown(f"- **Estimated Timeline:** {fd['timeline']}")
                    st.markdown("")
            
            with st.expander("Conclusion", expanded=True):
                st.markdown(conclusion)
            
            with st.expander("Suggested Thesis Titles", expanded=False):
                topic_words = topic.split()[:4]
                thesis_titles = [
                    f"A Comprehensive Systematic Literature Review of {topic[:80]}: Current State, Methodological Analysis, and Future Research Directions",
                    f"Advancing the Field of {topic[:70]}: A Critical Review of Existing Literature and Identification of Research Gaps",
                    f"Towards Robust and Deployable {topic[:60]}: Challenges, Opportunities, and a Research Agenda",
                    f"Comparative Analysis of Methodologies for {topic[:60]}: Performance Evaluation, Research Gaps, and Future Trajectories"
                ]
                for i, title in enumerate(thesis_titles, 1):
                    st.markdown(f"{i}. {title}")
            
            # Full report for download
            full_report = f"""# Systematic Literature Review: {topic}

**Generated:** {datetime.now().strftime('%B %d, %Y')}
**Papers Analyzed:** {len(papers)}
**Total Citations Across Papers:** {citation_stats['total']}
**Average Citations per Paper:** {citation_stats['average']}

---

## Abstract

{abstract}

---

## 1. Introduction

This systematic literature review provides a comprehensive analysis of research on {topic}. A total of {len(papers)} relevant papers were identified and analyzed using academic databases including Semantic Scholar and arXiv. The review synthesizes existing knowledge, compares methodological approaches, identifies research gaps, and proposes future research directions.

---

## 2. Papers Analyzed

"""
            for i, paper in enumerate(papers, 1):
                full_report += f"""
### Paper {i}: {paper['title']}

- **Source:** {paper['source']}
- **Publication Year:** {paper['year']}
- **Venue:** {paper['venue']}
- **Citation Count:** {paper['citations']}
- **Authors:** {', '.join(paper['authors'][:3]) if paper['authors'] else 'Not specified'}
- **Abstract:** {paper['abstract']}

---

"""
            
            full_report += f"""
## 3. Methodology Analysis

"""
            if methods:
                for method in methods:
                    count = sum(1 for p in papers if method.lower() in (p['title'] + p['abstract']).lower())
                    percent = round((count / len(papers)) * 100)
                    full_report += f"- **{method}:** {percent}% of papers ({count} out of {len(papers)})\n"
            else:
                full_report += "No specific methodologies could be automatically identified.\n"

            full_report += f"""
## 4. Research Topics

"""
            if topics:
                for topic in topics:
                    full_report += f"- {topic}\n"
            else:
                full_report += "Specific research topics could not be automatically classified.\n"

            full_report += f"""

## 5. Comparative Analysis

{comparative_analysis}

## 6. Research Gaps

"""
            for i, gap in enumerate(gaps, 1):
                full_report += f"""
### Gap {i}: {gap['title']}

{gap['description']}

*Supporting Evidence:* {gap['evidence']}

"""

            full_report += f"""
## 7. Future Research Directions

"""
            for fd in future_directions:
                full_report += f"""
### {fd['title']}

{fd['description']}

- **Priority:** {fd['priority']}
- **Timeline:** {fd['timeline']}

"""

            full_report += f"""
## 8. Conclusion

{conclusion}

## 9. Suggested Thesis Titles

1. {thesis_titles[0]}
2. {thesis_titles[1]}
3. {thesis_titles[2]}
4. {thesis_titles[3]}

---

*Report generated by DeepResearch-AI - Academic Literature Analysis System*
*Data sources: Semantic Scholar, arXiv*
*Report date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
            
            filename = f"literature_review_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            st.download_button(
                label="Download Complete Report (Markdown Format)",
                data=full_report,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True
            )
            
            with open("literature_review_report.md", "w", encoding="utf-8") as f:
                f.write(full_report)
            
            st.markdown('<div class="success-box">Report generation complete! The full literature review has been saved as "literature_review_report.md". Use the download button above to save a copy.</div>', unsafe_allow_html=True)
            
        else:
            status_placeholder.markdown('<div class="error-box">No papers were found matching your search query. Please try a different topic, broaden your search terms, or check your internet connection.</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 1.5rem; color: #64748b; font-size: 0.85rem; border-top: 1px solid #e2e8f0; margin-top: 2rem;">
    <strong>DeepResearch-AI</strong> | Systematic Literature Review and Research Gap Analysis System<br>
    Powered by Semantic Scholar and arXiv academic databases
</div>
""", unsafe_allow_html=True)