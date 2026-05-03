# Systematic Literature Review: Computer Vision

**Generated:** April 18, 2026
**Papers Analyzed:** 25
**Total Citations Across Papers:** 0
**Average Citations per Paper:** 0

---

## Abstract

This systematic literature review provides a comprehensive analysis of 25 research papers relevant to the specified research topic. The corpus includes 16 papers published since 2022, representing approximately 64 percent of the analyzed literature, indicating recent research activity in this domain. Citation analysis reveals limited research impact to date, which may indicate an emerging research area with significant growth potential. Key research areas identified in the literature include Remote Sensing, Prediction and Forecasting, Optimization, Mobile and Sensor Computing. Methodological analysis reveals that Mobile/Sensor-based, Deep Learning, Random Forest represent the dominant approaches employed in current research. This review synthesizes current knowledge, compares methodological approaches, identifies critical research gaps, and proposes future research directions to advance the field.

---

## 1. Introduction

This systematic literature review provides a comprehensive analysis of research on Computer Vision. A total of 25 relevant papers were identified and analyzed using academic databases including Semantic Scholar and arXiv. The review synthesizes existing knowledge, compares methodological approaches, identifies research gaps, and proposes future research directions.

---

## 2. Papers Analyzed


### Paper 1: GNSS Radio Occultation on Aerial Platforms with Commercial Off-The-Shelf Receivers

- **Source:** arXiv
- **Publication Year:** 2021
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Bryan C. Chan, Ashish Goel, Jonathan Kosh
- **Abstract:** In recent decades, GNSS Radio Occultation soundings have proven an invaluable input to global weather forecasting. The success of government-sponsored programs such as COSMIC is now complemented by commercial low-cost cubesat implementations. The result is access to more than 10,000 soundings per day and improved weather forecasting accuracy. This movement towards commercialization has been supported by several agencies, including the National Aeronautics and Space Administration (NASA), National Oceanic and Atmospheric Administration (NOAA) and the U.S. Air Force (USAF) with programs such as the Commercial Weather Data Pilot (CWDP). This has resulted in further interest in commercially deploying GNSS-RO on complementary platforms. Here, we examine a so far underutilized platform: the high-altitude weather balloon. Such meteorological radiosondes are deployed twice daily at over 900 locations globally and form an essential in-situ data source as a long-standing input to weather forecasting models. Adding GNSS-RO capability to existing radiosonde platforms would greatly expand capability, allowing for persistent and local area monitoring, a feature particularly useful for hurricane and other severe weather monitoring. A prohibitive barrier to entry to this inclusion is cost and complexity as GNSS-RO traditionally requires highly specialized and sensitive equipment. This paper describes a multi-year effort to develop a low-cost and scalable approach to balloon GNSS-RO based on Commercial-Off-The-Shelf (COTS) GNSS receivers. We present hardware prototypes and data processing techniques which demonstrate the technical feasibility of the approach through results from several flight testing campaigns.

---


### Paper 2: Standalone and RTK GNSS on 30,000 km of North American Highways

- **Source:** arXiv
- **Publication Year:** 2019
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Tyler G. R. Reid, Nahid Pervez, Umair Ibrahim
- **Abstract:** There is a growing need for vehicle positioning information to support Advanced Driver Assistance Systems (ADAS), Connectivity (V2X), and Automated Driving (AD) features. These range from a need for road determination (<5 meters), lane determination (<1.5 meters), and determining where the vehicle is within the lane (<0.3 meters). This work examines the performance of Global Navigation Satellite Systems (GNSS) on 30,000 km of North American highways to better understand the automotive positioning needs it meets today and what might be possible in the near future with wide area GNSS correction services and multi-frequency receivers. This includes data from a representative automotive production GNSS used primarily for turn-by-turn navigation as well as an Inertial Navigation System which couples two survey grade GNSS receivers with a tactical grade Inertial Measurement Unit (IMU) to act as ground truth. The latter utilized networked Real-Time Kinematic (RTK) GNSS corrections delivered over a cellular modem in real-time. We assess on-road GNSS accuracy, availability, and continuity. Availability and continuity are broken down in terms of satellite visibility, satellite geometry, position type (RTK fixed, RTK float, or standard positioning), and RTK correction latency over the network. Results show that current automotive solutions are best suited to meet road determination requirements at 98% availability but are less suitable for lane determination at 57%. Multi-frequency receivers with RTK corrections were found more capable with road determination at 99.5%, lane determination at 98%, and highway-level lane departure protection at 91%.

---


### Paper 3: Participatory Sensing for Localization of a GNSS Jammer

- **Source:** arXiv
- **Publication Year:** 2022
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Glädje Karl Olsson, Erik Axell, Erik G. Larsson
- **Abstract:** GNSS receivers are vulnerable to jamming and spoofing attacks, and numerous such incidents have been reported worldwide in the last decade. It is important to detect attacks fast and localize attackers, which can be hard if not impossible without dedicated sensing infrastructure. The notion of participatory sensing, or crowdsensing, is that a large ensemble of voluntary contributors provides the measurements, rather than relying on dedicated sensing infrastructure. This work considers embedded GNSS receivers to provide measurements for participatory jamming detection and localization. Specifically, this work proposes a novel jamming localization algorithm, based on participatory sensing, that exploits AGC and C/N_0 estimates from commercial GNSS receivers. The proposed algorithm does not require knowledge of the jamming power nor of the channels, but automatically estimates all parameters. The algorithm is shown to outperform similar state-of-the-art localization algorithms in relevant scenarios.

---


### Paper 4: Attitude-Estimation-Free GNSS and IMU Integration

- **Source:** arXiv
- **Publication Year:** 2023
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Taro Suzuki
- **Abstract:** A global navigation satellite system (GNSS) is a sensor that can acquire 3D position and velocity in an earth-fixed coordinate system and is widely used for outdoor position estimation of robots and vehicles. Various GNSS/inertial measurement unit (IMU) integration methods have been proposed to improve the accuracy and availability of GNSS positioning. However, all these methods require the addition of a 3D attitude to the estimated state to fuse the IMU data. In this study, we propose a new optimization-based positioning method for combining GNSS and IMU that does not require attitude estimation. The proposed method uses two types of constraints: one is a constraint between states using only the magnitude of the 3D acceleration observed by an accelerometer, and the other is a constraint on the angle between the velocity vectors using the angular change measured by a gyroscope. The evaluation results with the simulation data show that the proposed method maintains the position estimation accuracy even when the IMU mounting position error increases and improves the accuracy when the GNSS observations contain multipath errors or missing data. The proposed method could improve positioning accuracy in experiments using IMUs acquired in real environments.

---


### Paper 5: GNSS-R: Operational Applications

- **Source:** arXiv
- **Publication Year:** 2003
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** G. Ruffini, O. Germain, F. Soulat
- **Abstract:** This paper provides an overview of operational applications of GNSS-R, and describes Oceanpal, an inexpensive, all-weather, passive instrument for remote sensing of the ocean and other water surfaces. This instrument is based on the use of reflected signals emitted from GNSS, and it holds great potential for future applications thanks to the growing, long term GNSS infrastructure. The instrument exploits the fact that, at any given moment, several GNSS emitters are simultaneously in view, providing separated multiple scattering points with different geometries. Reflected signals are affected by surface roughness and motion (i.e., sea state, orbital motion, and currents), mean surface height and dielectric properties (i.e., salinity and pollution). Oceanpal is envisioned as an accurate, "dry" tide gauge and surface roughness monitoring system, and as an important element of a future distributed ocean remote sensing network concept. We also report some results from the Starlab Coastpal campaign, focusing on ground GNSS-R applications.

---


### Paper 6: GNSS Positioning using Cost Function Regulated Multilateration and Graph Neural Networks

- **Source:** arXiv
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Amir Jalalirad, Davide Belli, Bence Major
- **Abstract:** In urban environments, where line-of-sight signals from GNSS satellites are frequently blocked by high-rise objects, GNSS receivers are subject to large errors in measuring satellite ranges. Heuristic methods are commonly used to estimate these errors and reduce the impact of noisy measurements on localization accuracy. In our work, we replace these error estimation heuristics with a deep learning model based on Graph Neural Networks. Additionally, by analyzing the cost function of the multilateration process, we derive an optimal method to utilize the estimated errors. Our approach guarantees that the multilateration converges to the receiver's location as the error estimation accuracy increases. We evaluate our solution on a real-world dataset containing more than 100k GNSS epochs, collected from multiple cities with diverse characteristics. The empirical results show improvements from 40% to 80% in the horizontal localization error against recent deep learning baselines as well as classical localization approaches.

---


### Paper 7: Xona Pulsar Compatibility with GNSS

- **Source:** arXiv
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Tyler G. R. Reid, Matteo Gala, Mathieu Favreau
- **Abstract:** At least ten emerging providers are developing satellite navigation systems for low Earth orbit (LEO). Compatibility with existing GNSS in L-band is critical to their successful deployment and for the larger ecosystem. Xona is deploying Pulsar, a near 260-satellite LEO constellation offering dual L-band navigation services near L1 and L5. Designed for interoperability, Pulsar provides centimeter-level accuracy, resilience, and authentication, while maintaining a format that existing GNSS receivers can support through a firmware update. This study examines Pulsar's compatibility with GPS and Galileo by evaluating C/N0 degradation caused by the introduction of its X1 and X5 signals. Using spectrally compact QPSK modulation, Pulsar minimizes interference despite higher signal power. Theoretical analysis is supported by hardware testing across a range of commercial GNSS receivers in both lab-based simulation and in-orbit live-sky conditions. The study confirms Pulsar causes no adverse interference effects to existing GNSS, supporting coexistence and integration within the global PNT ecosystem.

---


### Paper 8: Robust Navigation In GNSS Degraded Environment Using Graph Optimization

- **Source:** arXiv
- **Publication Year:** 2018
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Ryan M. Watson, Jason N. Gross
- **Abstract:** Robust navigation in urban environments has received a considerable amount of both academic and commercial interest over recent years. This is primarily due to large commercial organizations such as Google and Uber stepping into the autonomous navigation market. Most of this research has shied away from Global Navigation Satellite System (GNSS) based navigation. The aversion to utilizing GNSS data is due to the degraded nature of the data in urban environment (e.g., multipath, poor satellite visibility). The degradation of the GNSS data in urban environments makes it such that traditional (GNSS) positioning methods (e.g., extended Kalman filter, particle filters) perform poorly. However, recent advances in robust graph theoretic based sensor fusion methods, primarily applied to Simultaneous Localization and Mapping (SLAM) based robotic applications, can also be applied to GNSS data processing. This paper will utilize one such method known as the factor graph in conjunction several robust optimization techniques to evaluate their applicability to robust GNSS data processing. The goals of this study are two-fold. First, for GNSS applications, we will experimentally evaluate the effectiveness of robust optimization techniques within a graph-theoretic estimation framework. Second, by releasing the software developed and data sets used for this study, we will introduce a new open-source front-end to the Georgia Tech Smoothing and Mapping (GTSAM) library for the purpose of integrating GNSS pseudorange observations.

---


### Paper 9: ZUPT Aided GNSS Factor Graph with Inertial Navigation Integration for Wheeled Robots

- **Source:** arXiv
- **Publication Year:** 2021
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Cagri Kilic, Shounak Das, Eduardo Gutierrez
- **Abstract:** In this work, we demonstrate the importance of zero velocity information for global navigation satellite system (GNSS) based navigation. The effectiveness of using the zero velocity information with zero velocity update (ZUPT) for inertial navigation applications have been shown in the literature. Here we leverage this information and add it as a position constraint in a GNSS factor graph. We also compare its performance to a GNSS/inertial navigation system (INS) coupled factor graph. We tested our ZUPT aided factor graph method on three datasets and compared it with the GNSS-only factor graph.

---


### Paper 10: How to Fight Fraudulent Publishing in the Mathematical Sciences: Joint Recommendations of the IMU and the ICIAM

- **Source:** arXiv
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Ilka Agricola, Lynn Heller, Wil Schilders
- **Abstract:** These recommendations were formulated by the authors in close collaboration with the IMU Committee on Publishing (chaired by Ilka Agricola) and have been endorsed by the Executive Committee of the IMU and the Board of the ICIAM in May/June 2025.

---


### Paper 11: Wheel-GINS: A GNSS/INS Integrated Navigation System with a Wheel-mounted IMU

- **Source:** arXiv
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Yibin Wu, Jian Kuang, Xiaoji Niu
- **Abstract:** A long-term accurate and robust localization system is essential for mobile robots to operate efficiently outdoors. Recent studies have shown the significant advantages of the wheel-mounted inertial measurement unit (Wheel-IMU)-based dead reckoning system. However, it still drifts over extended periods because of the absence of external correction signals. To achieve the goal of long-term accurate localization, we propose Wheel-GINS, a Global Navigation Satellite System (GNSS)/inertial navigation system (INS) integrated navigation system using a Wheel-IMU. Wheel-GINS fuses the GNSS position measurement with the Wheel-IMU via an extended Kalman filter to limit the long-term error drift and provide continuous state estimation when the GNSS signal is blocked. Considering the specificities of the GNSS/Wheel-IMU integration, we conduct detailed modeling and online estimation of the Wheel-IMU installation parameters, including the Wheel-IMU leverarm and mounting angle and the wheel radius error. Experimental results have shown that Wheel-GINS outperforms the traditional GNSS/Odometer/INS integrated navigation system during GNSS outages. At the same time, Wheel-GINS can effectively estimate the Wheel-IMU installation parameters online and, consequently, improve the localization accuracy and practicality of the system. The source code of our implementation is publicly available (https://github.com/i2Nav-WHU/Wheel-GINS).

---


### Paper 12: Supporting GNSS Baseband Using Smartphone IMU and Ultra-Tight Integration

- **Source:** arXiv
- **Publication Year:** 2021
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Yiran Luo, You Li, Jin Wang
- **Abstract:** A great surge in the development of global navigation satellite systems (GNSS) excavates the potential for prosperity in many state-of-the-art technologies, e.g., autonomous ground vehicle navigation. Nevertheless, the GNSS is vulnerable to various ground interferences, which significantly break down the continuity of the navigation system. Meanwhile, the GNSS-based next-generation navigation devices are being developed to be smaller, more low-cost, and lightweight, as the commercial market forecasts. This work aims to answer whether the smartphone inertial measurement unit (IMU) is sufficient to support the GNSS baseband. Thus, a cascaded ultra-tightly coupled GNSS/inertial navigation system (INS) technique, where consumer-level smartphone sensors are used, is applied to improve the baseband of GNSS software-defined radios (SDRs). A Doppler value is predicted based on an integrated extended Kalman filter (EKF) navigator where the pseudorange-state-based measurements of GNSS and INS are fused. It is used to assist numerically controlled oscillators (NCOs) in the GNSS baseband. Then, an ultra-tight integration platform is built with the upgraded GNSS SDR, of which baseband processing is integrated with INS mechanization. Finally, tracking and carrier-based positioning performances are assessed in the proposed platform for the smartphone-IMU-aided GNSS baseband via kinematic field tests. The experimental results prove that extra hardware with only a few dollars instead of more expensive ones can improve the GNSS baseband efficiently.

---


### Paper 13: PARFAIT: GNSS-R coastal altimetry

- **Source:** arXiv
- **Publication Year:** 2003
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** M. Caparrini, L. Ruffini, G. Ruffini
- **Abstract:** GNSS-R signals contain a coherent and an incoherent component. A new algorithm for coherent phase altimetry over rough ocean surfaces, called PARFAIT, has been developed and implemented in Starlab's STARLIGHT GNSS-R software package. In this paper we report our extraction and analysis of the coherent component of L1 GPS-R signals collected during the ESTEC Bridge 2 experimental campaign using this technique. The altimetric results have been compared with a GPS-buoy calibrated tide model with a resulting precision of the order 1 cm.

---


### Paper 14: PRIMUS: Pretraining IMU Encoders with Multimodal Self-Supervision

- **Source:** arXiv
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Arnav M. Das, Chi Ian Tang, Fahim Kawsar
- **Abstract:** Sensing human motions through Inertial Measurement Units (IMUs) embedded in personal devices has enabled significant applications in health and wellness. Labeled IMU data is scarce, however, unlabeled or weakly labeled IMU data can be used to model human motions. For video or text modalities, the "pretrain and adapt" approach utilizes large volumes of unlabeled or weakly labeled data to build a strong feature extractor, followed by adaptation to specific tasks using limited labeled data. However, pretraining methods are poorly understood for IMU data, and pipelines are rarely evaluated on out-of-domain tasks. We propose PRIMUS: a method for PRetraining IMU encoderS that uses a novel pretraining objective that is empirically validated based on downstream performance on both in-domain and out-of-domain datasets. The PRIMUS objective effectively enhances downstream performance by combining self-supervision, multimodal, and nearest-neighbor supervision. With fewer than 500 labeled samples per class, PRIMUS improves test accuracy by up to 15%, compared to state-of-the-art baselines. To benefit the broader community, we have open-sourced our code at github.com/nokia-bell-labs/pretrained-imu-encoders.

---


### Paper 15: Real-time loosely coupled GNSS and IMU integration via Factor Graph Optimization

- **Source:** arXiv
- **Publication Year:** 2026
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Radu-Andrei Cioaca, Cristian Rusu, Paul Irofti
- **Abstract:** Accurate positioning, navigation, and timing (PNT) is fundamental to the operation of modern technologies and a key enabler of autonomous systems. A very important component of PNT is the Global Navigation Satellite System (GNSS) which ensures outdoor positioning. Modern research directions have pushed the performance of GNSS localization to new heights by fusing GNSS measurements with other sensory information, mainly measurements from Inertial Measurement Units (IMU). In this paper, we propose a loosely coupled architecture to integrate GNSS and IMU measurements using a Factor Graph Optimization (FGO) framework. Because the FGO method can be computationally challenging and often used as a post-processing method, our focus is on assessing its localization accuracy and service availability while operating in real-time in challenging environments (urban canyons). Experimental results on the UrbanNav-HK-MediumUrban-1 dataset show that the proposed approach achieves real-time operation and increased service availability compared to batch FGO methods. While this improvement comes at the cost of reduced positioning accuracy, the paper provides a detailed analysis of the trade-offs between accuracy, availability, and computational efficiency that characterize real-time FGO-based GNSS/IMU fusion.

---


### Paper 16: Adaptive Factor Graph-Based Tightly Coupled GNSS/IMU Fusion for Robust Positionin

- **Source:** arXiv
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Elham Ahmadi, Alireza Olama, Petri Välisuo
- **Abstract:** Reliable positioning in GNSS-challenged environments remains a critical challenge for navigation systems. Tightly coupled GNSS/IMU fusion improves robustness but remains vulnerable to non-Gaussian noise and outliers. We present a robust and adaptive factor graph-based fusion framework that directly integrates GNSS pseudorange measurements with IMU preintegration factors and incorporates the Barron loss, a general robust loss function that unifies several m-estimators through a single tunable parameter. By adaptively down weighting unreliable GNSS measurements, our approach improves resilience positioning. The method is implemented in an extended GTSAM framework and evaluated on the UrbanNav dataset. The proposed solution reduces positioning errors by up to 41% relative to standard FGO, and achieves even larger improvements over extended Kalman filter (EKF) baselines in urban canyon environments. These results highlight the benefits of Barron loss in enhancing the resilience of GNSS/IMU-based navigation in urban and signal-compromised environments.

---


### Paper 17: Towards Scale-Aware, Robust, and Generalizable Unsupervised Monocular Depth Estimation by Integrating IMU Motion Dynamics

- **Source:** arXiv
- **Publication Year:** 2022
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Sen Zhang, Jing Zhang, Dacheng Tao
- **Abstract:** Unsupervised monocular depth and ego-motion estimation has drawn extensive research attention in recent years. Although current methods have reached a high up-to-scale accuracy, they usually fail to learn the true scale metric due to the inherent scale ambiguity from training with monocular sequences. In this work, we tackle this problem and propose DynaDepth, a novel scale-aware framework that integrates information from vision and IMU motion dynamics. Specifically, we first propose an IMU photometric loss and a cross-sensor photometric consistency loss to provide dense supervision and absolute scales. To fully exploit the complementary information from both sensors, we further drive a differentiable camera-centric extended Kalman filter (EKF) to update the IMU preintegrated motions when observing visual measurements. In addition, the EKF formulation enables learning an ego-motion uncertainty measure, which is non-trivial for unsupervised methods. By leveraging IMU during training, DynaDepth not only learns an absolute scale, but also provides a better generalization ability and robustness against vision degradation such as illumination change and moving objects. We validate the effectiveness of DynaDepth by conducting extensive experiments and simulations on the KITTI and Make3D datasets.

---


### Paper 18: Real-time tightly coupled GNSS and IMU integration via Factor Graph Optimization

- **Source:** arXiv
- **Publication Year:** 2026
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Radu-Andrei Cioaca, Paul Irofti, Cristian Rusu
- **Abstract:** Reliable positioning in dense urban environments remains challenging due to frequent GNSS signal blockage, multipath, and rapidly varying satellite geometry. While factor graph optimization (FGO)-based GNSS-IMU fusion has demonstrated strong robustness and accuracy, most formulations remain offline. In this work, we present a real-time tightly coupled GNSS-IMU FGO method that enables causal state estimation via incremental optimization with fixed-lag marginalization, and we evaluate its performance in a highly urbanized GNSS-degraded environment using the UrbanNav dataset.

---


### Paper 19: LiDAR, GNSS and IMU Sensor Fine Alignment through Dynamic Time Warping to Construct 3D City Maps

- **Source:** arXiv
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Haitian Wang, Hezam Albaqami, Xinyu Wang
- **Abstract:** LiDAR-based 3D mapping suffers from cumulative drift causing global misalignment, particularly in GNSS-constrained environments. To address this, we propose a unified framework that fuses LiDAR, GNSS, and IMU data for high-resolution city-scale mapping. The method performs velocity-based temporal alignment using Dynamic Time Warping and refines GNSS and IMU signals via extended Kalman filtering. Local maps are built using Normal Distributions Transform-based registration and pose graph optimization with loop closure detection, while global consistency is enforced using GNSS-constrained anchors followed by fine registration of overlapping segments. We also introduce a large-scale multimodal dataset captured in Perth, Western Australia to facilitate future research in this direction. Our dataset comprises 144,000 frames acquired with a 128-channel Ouster LiDAR, synchronized RTK-GNSS trajectories, and MEMS-IMU measurements across 21 urban loops. To assess geometric consistency, we evaluated our method using alignment metrics based on road centerlines and intersections to capture both global and local accuracy. The proposed framework reduces the average global alignment error from 3.32m to 1.24m, achieving a 61.4% improvement, and significantly decreases the intersection centroid offset from 13.22m to 2.01m, corresponding to an 84.8% enhancement. The constructed high-fidelity map and raw dataset are publicly available through https://ieee-dataport.org/documents/perth-cbd-high-resolution-lidar-map-gnss-and-imu-calibration, and its visualization can be viewed at https://www.youtube.com/watch?v=-ZUgs1KyMks. The source code is available at https://github.com/HaitianWang/LiDAR-GNSS-and-IMU-Sensor-Fine-Alignment-through-Dynamic-Time-Warping-to-Construct-3D-City-Maps. This dataset and method together establish a new benchmark for evaluating 3D city mapping in GNSS-constrained environments.

---


### Paper 20: Online IMU-odometer Calibration using GNSS Measurements for Autonomous Ground Vehicle Localization

- **Source:** arXiv
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Baoshan Song, Xiao Xia, Penggao Yan
- **Abstract:** Accurate calibration of intrinsic (odometer scaling factors) and extrinsic parameters (IMU-odometer translation and rotation) is essential for autonomous ground vehicle localization. Existing GNSS-aided approaches often rely on positioning results or raw measurements without ambiguity resolution, and their observability properties remain underexplored. This paper proposes a tightly coupled online calibration method that fuses IMU, odometer, and raw GNSS measurements (pseudo-range, carrier-phase, and Doppler) within an extendable factor graph optimization (FGO) framework, incorporating outlier mitigation and ambiguity resolution. Observability analysis reveals that two horizontal translation and three rotation parameters are observable under general motion, while vertical translation remains unobservable. Simulation and real-world experiments demonstrate superior calibration and localization performance over state-of-the-art loosely coupled methods. Specifically, the IMU-odometer positioning using our calibrated parameters achieves the absolute maximum error of 17.75 m while the one of LC method is 61.51 m, achieving up to 71.14 percent improvement. To foster further research, we also release the first open-source dataset that combines IMU, 2D odometer, and raw GNSS measurements from both rover and base stations.

---


### Paper 21: Carrier-phase and IMU based GNSS Spoofing Detection for Ground Vehicles

- **Source:** arXiv
- **Publication Year:** 2022
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Zachary Clements, James E. Yoder, Todd E. Humphreys
- **Abstract:** This paper develops, implements, and validates a powerful single-antenna carrier-phase-based test to detect Global Navigation Satellite Systems (GNSS) spoofing attacks on ground vehicles equipped with a low-cost inertial measurement unit (IMU). Increasingly-automated ground vehicles require precise positioning that is resilient to unusual natural or accidental events and secure against deliberate attack. This paper's spoofing detection technique capitalizes on the carrier-phase fixed-ambiguity residual cost produced by a well-calibrated carrier-phase-differential GNSS (CDGNSS) estimator that is tightly coupled with a low-cost IMU. The carrier-phase fixed-ambiguity residual cost is sensitive at the sub-centimeter-level to discrepancies between measured carrier phase values and the values predicted by prior measurements and by the dynamics model, which is based on IMU measurements and on vehicle constraints. Such discrepancies will arise in a spoofing attack due to the attacker's practical inability to predict the centimeter-amplitude vehicle movement caused by roadway irregularities. The effectiveness of the developed spoofing detection method is evaluated with data captured by a vehicle-mounted sensor suite in Austin, Texas. The dataset includes both consumer- and industrial-grade IMU data and a diverse set of multipath environments (open sky, shallow urban, and deep urban). Artificial worst-case spoofing attacks injected into the dataset are detected within two seconds.

---


### Paper 22: The GNSS-R Eddy Experiment I: Altimetry from Low Altitude Aircraft

- **Source:** arXiv
- **Publication Year:** 2003
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** G. Ruffini, F. Soulat, M. Caparrini
- **Abstract:** We report results from the Eddy Experiment, where a synchronous GPS receiver pair was flown on an aircraft to collect sampled L1 signals and their reflections from the sea surface to investigate the altimetric accuracy of GNSS-R. During the experiment, surface wind speed (U10) was of the order of 10 m/s, and significant wave heights of up to 2 m, as discussed further in a companion paper. After software tracking of the two signals through despreading of the GPS codes, a parametric waveform model containing the description of the sea surface conditions has been used to fit the waveforms (retracking) and estimate the temporal lapse between the direct GPS signals and their reflections. The estimated lapses have then been used to estimate the sea surface height (SSH) along the aircraft track using a differential geometric model. As expected, the precision of GNSS-R ranges was of 3 m after 1 second integration. More importantly, the accuracy of the GNSS-R altimetric solution with respect to Jason-1 SSH and in situ GPS buoy measurements was of 10 cm, which was the target with the used experimental setup. This new result confirms the potential of GNSS-R for mesoscale altimetric monitoring of the ocean, and provides an important milestone on the road to a space mission.

---


### Paper 23: Few-Shot Learning with Uncertainty-based Quadruplet Selection for Interference Classification in GNSS Data

- **Source:** arXiv
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Felix Ott, Lucas Heublein, Nisha Lakshmana Raichur
- **Abstract:** Jamming devices pose a significant threat by disrupting signals from the global navigation satellite system (GNSS), compromising the robustness of accurate positioning. Detecting anomalies in frequency snapshots is crucial to counteract these interferences effectively. The ability to adapt to diverse, unseen interference characteristics is essential for ensuring the reliability of GNSS in real-world applications. In this paper, we propose a few-shot learning (FSL) approach to adapt to new interference classes. Our method employs quadruplet selection for the model to learn representations using various positive and negative interference classes. Furthermore, our quadruplet variant selects pairs based on the aleatoric and epistemic uncertainty to differentiate between similar classes. We recorded a dataset at a motorway with eight interference classes on which our FSL method with quadruplet loss outperforms other FSL techniques in jammer classification accuracy with 97.66%. Dataset available at: https://gitlab.cc-asp.fraunhofer.de/darcy_gnss/FIOT_highway

---


### Paper 24: Vehicle Fuel Consumption Virtual Sensing from GNSS and IMU Measurements

- **Source:** arXiv
- **Publication Year:** 2023
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Marcello Cellina, Silvia Strada, Sergio Matteo Savaresi
- **Abstract:** This paper presents a vehicle-independent, non-intrusive, and light monitoring system for accurately measuring fuel consumption in road vehicles from longitudinal speed and acceleration derived continuously in time from GNSS and IMU sensors mounted inside the vehicle. In parallel to boosting the transition to zero-carbon cars, there is an increasing interest in low-cost instruments for precise measurement of the environmental impact of the many internal combustion engine vehicles still in circulation. The main contribution of this work is the design and comparison of two innovative black-box algorithms, one based on a reduced complexity physics modeling while the other relying on a feedforward neural network for black-box fuel consumption estimation using only velocity and acceleration measurements. Based on suitable metrics, the developed algorithms outperform the state of the art best approach, both in the instantaneous and in the integral fuel consumption estimation, with errors smaller than 1\% with respect to the fuel flow ground truth. The data used for model identification, testing, and experimental validation is composed of GNSS velocity and IMU acceleration measurements collected during several trips using a diesel fuel vehicle on different roads, in different seasons, and with varying numbers of passengers. Compared to built-in vehicle monitoring systems, this methodology is not customized, uses off-the-shelf sensors, and is based on two simple algorithms that have been validated offline and could be easily implemented in a real-time environment.

---


### Paper 25: Fusing Wearable IMUs with Multi-View Images for Human Pose Estimation: A Geometric Approach

- **Source:** arXiv
- **Publication Year:** 2020
- **Venue:** arXiv Preprint
- **Citation Count:** 0
- **Authors:** Zhe Zhang, Chunyu Wang, Wenhu Qin
- **Abstract:** We propose to estimate 3D human pose from multi-view images and a few IMUs attached at person's limbs. It operates by firstly detecting 2D poses from the two signals, and then lifting them to the 3D space. We present a geometric approach to reinforce the visual features of each pair of joints based on the IMUs. This notably improves 2D pose estimation accuracy especially when one joint is occluded. We call this approach Orientation Regularized Network (ORN). Then we lift the multi-view 2D poses to the 3D space by an Orientation Regularized Pictorial Structure Model (ORPSM) which jointly minimizes the projection error between the 3D and 2D poses, along with the discrepancy between the 3D pose and IMU orientations. The simple two-step approach reduces the error of the state-of-the-art by a large margin on a public dataset. Our code will be released at https://github.com/CHUNYUWANG/imu-human-pose-pytorch.

---


## 3. Methodology Analysis

- **Mobile/Sensor-based:** 0% of papers (0 out of 25)
- **Deep Learning:** 4% of papers (1 out of 25)
- **Random Forest:** 0% of papers (0 out of 25)
- **Sensor Fusion:** 4% of papers (1 out of 25)

## 4. Research Topics

- Remote Sensing
- Prediction and Forecasting
- Optimization
- Mobile and Sensor Computing
- Detection and Classification
- Computer Vision


## 5. Comparative Analysis

### Comparative Analysis of 25 Research Papers

**Most Influential Papers Based on Citation Count**

No papers with significant citations were found in this search. This may indicate an emerging research area or niche topic.

**Methodology Distribution Across Analyzed Papers**

- **Deep Learning:** Used in 1 out of 25 papers, representing 4% of the analyzed literature.
- **Sensor Fusion:** Used in 1 out of 25 papers, representing 4% of the analyzed literature.

**Key Observations from the Comparative Analysis**

- None of the 25 papers analyzed have received citations yet, suggesting this may be a newly emerging research area.
- Recent research activity is evident with 13 papers published since 2023, indicating growing interest in this domain.
- Mobile/Sensor-based emerges as the predominant methodology, though direct performance comparison across studies remains challenging due to varying evaluation protocols and datasets.
- A notable observation is the lack of standardized benchmark datasets and evaluation metrics, which currently limits fair comparison between different approaches.


## 6. Research Gaps


### Gap 1: Limited High-Impact Research

Out of 25 papers analyzed, only 0 papers have received significant citation impact (more than 10 citations). This indicates that the research field is still in its early stages or that existing work has not yet achieved widespread recognition or adoption. Future research should focus on producing high-quality, reproducible studies that can serve as foundational work for the community.

*Supporting Evidence:* Citation analysis shows 0 out of 25 papers have more than 10 citations


### Gap 2: Lack of Methodological Standardization

The literature employs diverse methodologies including Mobile/Sensor-based, Deep Learning, Random Forest. However, there is no standardized evaluation framework or benchmark dataset that allows fair comparison between these different approaches. Each study uses its own experimental setup, dataset, and evaluation metrics, making it difficult to determine which methodology performs best under comparable conditions.

*Supporting Evidence:* 4 different methodologies identified across 25 papers without unified evaluation standards


### Gap 3: Need for Comprehensive Evaluation Frameworks

Based on the analysis of 25 papers, there is a clear need for establishing comprehensive evaluation frameworks that include standardized benchmarks, reproducible experimental protocols, and fair comparison metrics. Such frameworks would accelerate progress by enabling direct comparison of different approaches and identifying the most promising research directions.

*Supporting Evidence:* Analysis of 25 papers reveals inconsistent evaluation methodologies


## 7. Future Research Directions


### Addressing the Limited High-Impact Research

The primary research gap identified in this review is the limited high-impact research. To address this gap, future research should focus on Out of 25 papers analyzed, only 0 papers have received significant citation impact (more than 10 citations). This indicates that the research field is More specifically, researchers should design studies that directly target this gap with clear experimental validation.

- **Priority:** High Priority
- **Timeline:** 6 to 9 months


### Advancing Mobile/Sensor-based for This Domain

Mobile/Sensor-based currently represents the most frequently used methodology in the analyzed literature. However, there remains significant room for optimization and adaptation to the specific requirements of this research domain. Future work should explore hybrid approaches that combine Mobile/Sensor-based with complementary techniques, as well as investigate parameter tuning and architectural innovations to improve performance.

- **Priority:** High Priority
- **Timeline:** 6 to 12 months


### Establishing Performance Baselines

The current literature lacks clear performance baselines and benchmarks. Future research should first focus on establishing standardized evaluation protocols and reporting performance metrics consistently. This foundational work would enable meaningful comparisons and help identify the most promising research directions for subsequent investigation.

- **Priority:** High Priority
- **Timeline:** 3 to 6 months


### Cross-Domain Validation and Generalization Studies

Current research predominantly focuses on specific datasets or controlled conditions. Future work must extend validation across diverse domains, environments, and data distributions. This includes conducting rigorous cross-dataset evaluations, investigating domain adaptation techniques, and studying model robustness under varying real-world conditions. Such studies are essential for determining the practical applicability and limitations of proposed methods.

- **Priority:** Medium Priority
- **Timeline:** 9 to 12 months


### Real-World Deployment and Field Validation

Moving beyond laboratory settings to real-world deployment represents a critical next step for this research domain. Future studies should include field trials, deployment case studies, and practical application evaluations. This includes addressing challenges related to scalability, latency, resource constraints, and system integration that are often overlooked in controlled experimental settings.

- **Priority:** High Priority
- **Timeline:** 12 to 18 months


## 8. Conclusion

This literature review analyzed 25 research papers to assess the current state of research. Key finding one: None of the analyzed papers have received significant citation impact, indicating that this is an emerging research area with substantial potential for foundational contributions. Key finding two: 16 papers (approximately 64 percent) were published in the last two years, demonstrating growing research interest and recent momentum in this domain. Key finding four: Critical research gaps identified include Limited High-Impact Research, Lack of Methodological Standardization, Need for Comprehensive Evaluation Frameworks. These gaps represent significant opportunities for future investigation and potential breakthroughs. In conclusion, while progress has been made in this research domain, substantial opportunities remain for advancing the field through addressing the identified gaps and pursuing the proposed future research directions.

## 9. Suggested Thesis Titles

1. A Comprehensive Systematic Literature Review of Computer Vision: Current State, Methodological Analysis, and Future Research Directions
2. Advancing the Field of Computer Vision: A Critical Review of Existing Literature and Identification of Research Gaps
3. Towards Robust and Deployable Computer Vision: Challenges, Opportunities, and a Research Agenda
4. Comparative Analysis of Methodologies for Computer Vision: Performance Evaluation, Research Gaps, and Future Trajectories

---

*Report generated by DeepResearch-AI - Academic Literature Analysis System*
*Data sources: Semantic Scholar, arXiv*
*Report date: 2026-04-18 01:44:00*
