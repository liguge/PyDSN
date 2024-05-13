# Interpretable modulated differentiable STFT and physics-informed balanced spectrum metric for freight train wheelset bearing cross-machine transfer fault diagnosis under speed fluctuations

🔥 The pytorch implementation of the paper [Interpretable modulated differentiable STFT and physics-informed balanced spectrum metric for freight train wheelset bearing cross-machine transfer fault diagnosis under speed fluctuations](https://doi.org/10.1016/j.aei.2024.102568)



# 

## Brief introduction  
The service conditions of wheelset bearings has a direct impact on the safe operation of railway heavy haul freight trains as the key components. However, speed fluctuation of the trains and few fault samples are the two main problems that restrict the accuracy of bearing fault diagnosis. Therefore, a cross-machine transfer diagnosis (pyDSN) network coupled with interpretable modulated differentiable short-time Fourier transform (STFT) and physics-informed balanced spectrum quality metric is proposed to learn domain-invariant and discriminative features under time-varying speeds. Firstly, due to insufficiency in extracting extract frequency components of time-varying speed signals using fixed windows, a modulated differentiable STFT (MDSTFT) that is interpretable with STFT-informed theoretical support, is proposed to extract the robust time–frequency spectrum (TFS). During training process, multiple windows with different lengths dynamically change. Also, in addition to the classification metric and domain discrepancy metric, we creatively introduce a third kind of metric, referred to as the physics-informed metric, to enhance transferable TFS. A physics-informed balanced spectrum quality (BSQ) regularization loss is devised to guide an optimization direction for MDSTFT and model. With it, not only can model acquire high-quality TFS, but also a physics-restricted domain adaptation network can be also acquired, making it learn real-world physics knowledge, ultimately diminish the domain discrepancy across different datasets. The experiment is conducted in the scenario of migrating from the laboratory datasets to the freight train dataset, indicating that the hybrid-driven pyDSN outperforms existing methods and has practical value. Partial code is availble at https://github.com/liguge/PyDSN.

## Highlights

- A pyDSN is proposed for heavy haul freight train wheelset bearing transfer diagnosis.
- pyDSN can tackle cross-machine transfer diagnosis under speed fluctuations.
- The modulation differentiable STFT incorporated a mask modulation mechanism.
- Balanced spectrum is devised to evaluate the quality of spectrograms.
- The interpretability of MDSTFT is elaborated from both quantitative and qualitative perspectives.


## Paper
Interpretable modulated differentiable STFT and physics-informed balanced spectrum metric for freight train wheelset bearing cross-machine transfer fault diagnosis under speed fluctuations 

Chao He<sup>a,b</sup>, **Hongmei Shi<sup>a,b,*</sup>**, Ruixin Li<sup>c</sup>, Jianbo Li<sup>a,b</sup>, ZuJun Yu<sup>a,b</sup>

<sup>a</sup>State Key Laboratory of Advanced Rail Autonomous Operation, Beijing Jiaotong University, Beijing 100044, China 

<sup>b</sup>School of Mechanical, Electronic and Control Engineering, Beijing Jiaotong University, Beijing 100044, China

[Advanced Engineering Informatics](https://www.sciencedirect.com/journal/advanced-engineering-informatics/vol/62/part/PA)



## Citation

```html
@article{He_2024, 
title={Interpretable modulated differentiable STFT and physics-informed balanced spectrum metric for freight train wheelset bearing cross-machine transfer fault diagnosis under speed fluctuations}, 
volume={62}, 
DOI={10.1016/j.aei.2024.102568}, 
journal={Advanced Engineering Informatics}, 
author={He, Chao and Shi, Hongmei and Li, Ruixin and Li, Jianbo and Yu, ZuJun}, 
year={2024}, 
pages={102568} 
}

```

C. He, H. Shi, R. Li, J. Li, Z. Yu, Interpretable modulated differentiable STFT and physics-informed balanced spectrum metric for freight train wheelset bearing cross-machine transfer fault diagnosis under speed fluctuations, Advanced Engineering Informatics 62 (2024) 102568, https://doi.org/10.1016/j.aei.2024.102568




## Ackowledgements
The authors are grateful for the supports of the National Natural Science Foundation of China (No. 52272429), and State Key Laboratory of Advanced Rail Autonomous Operation (Contract No. RAO2023ZZ003).



## Contact

- **Chao He**
- **chaohe#bjtu.edu.cn (please replace # by @)**

​      
