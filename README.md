# Interpretable Modulated Differentiable STFT and Physics-informed Balanced Spectrum Metric for Freight Train Wheelset Bearing Cross-machine Transfer Fault Diagnosis under Speed Fluctuations

The pytorch implementation of the paper [Interpretable Physics-informed Domain Adaptation Paradigm for Cross-machine Transfer Diagnosis](https://doi.org/10.1016/j.knosys.2024.111499)



# Result!

The code is based on UDTL and the PU dataset, and the accuracy can be improved from 63.79% to 77.19%, an increase of 13.40%.

- Baseline(**Line 183 in resnet_18.py**)

  ![image-20240405212227670](G:\研究生资料\博士\投稿论文\第三篇\image-20240405212227670.png)

- Weight initialization

  ![image-20240405212209638](G:\研究生资料\博士\投稿论文\第三篇\image-20240405212209638.png)

## Brief introduction  
The service conditions of wheelset bearings has a direct impact on the safe operation of railway heavy haul freight trains as the key components. However, speed fluctuation of the trains and few fault samples are the two main problems that restrict the accuracy of bearing fault diagnosis. Therefore, a cross-machine transfer diagnosis (pyDSN) network coupled with interpretable modulated differentiable short-time Fourier transform (STFT) and physics-informed balanced spectrum quality metric is proposed to learn domain-invariant and discriminative features under time-varying speeds. Firstly, due to insufficiency in extracting extract frequency components of time-varying speed signals using fixed windows, a modulated differentiable STFT (MDSTFT) that is interpretable with STFT-informed theoretical support, is proposed to extract the robust time–frequency spectrum (TFS). During training process, multiple windows with different lengths dynamically change. Also, in addition to the classification metric and domain discrepancy metric, we creatively introduce a third kind of metric, referred to as the physics-informed metric, to enhance transferable TFS. A physics-informed balanced spectrum quality (BSQ) regularization loss is devised to guide an optimization direction for MDSTFT and model. With it, not only can model acquire high-quality TFS, but also a physics-restricted domain adaptation network can be also acquired, making it learn real-world physics knowledge, ultimately diminish the domain discrepancy across different datasets. The experiment is conducted in the scenario of migrating from the laboratory datasets to the freight train dataset, indicating that the hybrid-driven pyDSN outperforms existing methods and has practical value. Partial code is availble at https://github.com/liguge/PyDSN.

## Highlights

- A first-layer kernel with wavelet weights is designed to diminish domain discrepancy.
- Optimized wavelet weights are devised as the first-layer initialization.
- The dual-stream module is designed to promote the domain transferability.
- A paradigm for transfer diagnosis is posed to design the first convolutional layer.
- The availability of WIDAN is validated with four data sources.


## Paper
Interpretable Physics-informed Domain Adaptation Paradigm for Cross-machine Transfer Diagnosis

Chao He<sup>a,b</sup>, **Hongmei Shi<sup>a,b,*</sup>**, Xiaorong Liu<sup>c</sup> and Jianbo Li<sup>a,b</sup>

<sup>a</sup>State Key Laboratory of Advanced Rail Autonomous Operation, Beijing Jiaotong University, Beijing 100044, China 

<sup>b</sup>School of Mechanical, Electronic and Control Engineering, Beijing Jiaotong University, Beijing 100044, China

<sup>c</sup>School of Computing and Artificial Intelligence, Southwest Jiaotong University, Chengdu 611756, China

[Knowledge-Based Systems](https://www.sciencedirect.com/journal/knowledge-based-systems/vol/288/suppl/C)



## Citation

```html
@article{he2024interpretable,
  title={Interpretable physics-informed domain adaptation paradigm for cross-machine transfer diagnosis},
  author={He, Chao and Shi, Hongmei and Liu, Xiaorong and Li, Jianbo},
  journal={Knowledge-Based Systems},
  volume={288},
  pages={111499},
  year={2024},
  doi={10.1016/j.knosys.2024.111499}
}
```

C. He, H. Shi, X. Liu, J. Li, Interpretable Physics-informed Domain Adaptation Paradigm for Cross-machine Transfer Diagnosis, Knowledge-Based Systems 288 (2024) 111499, https://doi.org/10.1016/j.knosys.2024.111499




## Ackowledgements
The authors are grateful for the supports of the National Natural Science Foundation of China (No. 52272429), and State Key Laboratory of Advanced Rail Autonomous Operation (Contract No. RAO2023ZZ003).



## Contact

- **Chao He**
- **chaohe#bjtu.edu.cn (please replace # by @)**

​      
