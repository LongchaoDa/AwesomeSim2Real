# AwesomeSim2Real

## Sim-to-Real-Paper-Collection


In the paper collection, we collected RL-based sim-to-real papers published in the recent years (201x-202x) on top conferences and journals, and categorize based on the research domains, namely simulators, robotics, transportations and others.



- [Sim-to-Real Paper Collection](#sim-to-real-paper-collection)
  - [Surveys and Simulators](#surveys-and-simulators)
    - [Survey Papers](#survey-papers)
    - [Environments and Benchmarks](#environments-and-benchmarks)
      - [Robotics Environments](#robotics-environments)
      - [Robotics Benchmarks](#robotics-benchmarks)
      - [Transportation Environments](#transportation-environments)
      - [Transportation Benchmarks](#transportation-benchmarks)
      - [Recommender System Environments](#recommender-system-environments)
      - [Recommender System Benchmarks](#recommender-system-benchmarks)
      - [Other Environments](#other-environments)
      - [Other Benchmarks](#other-benchmarks)
  - [Technique Papers](#technique-papers)
    - [Obeservation](#obeservation)
    - [Action](#action)
    - [Transistion](#transistion)
    - [Reward](#reward)


## Surveys and Simulators

### Survey Papers
1. **A Survey on Sim-to-Real Transfer Methods for Robotic Manipulation**. *Pitkevich, Andrei and Makarov, Ilya*. IEEE 22nd Jubilee International Symposium on Intelligent Systems and Informatics (SISY). 2024. [link](https://www.researchgate.net/publication/385575540_A_Survey_on_Sim-to-Real_Transfer_Methods_for_Robotic_Manipulation)
1. **How simulation helps autonomous driving: A survey of sim2real, digital twins, and parallel intelligence**. *Hu, Xuemin and Li, Shen and Huang, Tingyu and Tang, Bo and Huai, Rouxing and Chen, Long*. IEEE Transactions on Intelligent Vehicles. 2023. [link](https://ieeexplore.ieee.org/document/10242366)
1. **Parallel learning: Overview and perspective for computational learning across Syn2Real and Sim2Real**. *HMiao, Qinghai and Lv, Yisheng and Huang, Min and Wang, Xiao and Wang, Fei-Yue*. IEEE/CAA Journal of Automatica Sinica. 2023. [link](https://ieeexplore.ieee.org/document/10057176)
1. **A Brief Survey of Sim2Real Methods for Robot Learning**. *Dimitropoulos, Konstantinos and Hatzilygeroudis, Ioannis and Chatzilygeroudis, Konstantinos*. International Conference on Robotics in Alpe-Adria Danube Region. 2022 [link](https://link.springer.com/chapter/10.1007/978-3-031-04870-8_16)
1. **A survey of sim-to-real transfer techniques applied to reinforcement learning for bioinspired robots**. *Zhu, Wei and Guo, Xian and Owaki, Dai and Kutsuzawa, Kyo and Hayashibe, Mitsuhiro*. IEEE Transactions on Neural Networks and Learning Systems. 2021 [link](https://ieeexplore.ieee.org/document/9552429)
1. **Crossing the reality gap: A survey on sim-to-real transferability of robot controllers in reinforcement learning**. *Salvato, Erica and Fenu, Gianfranco and Medvet, Eric and Pellegrino, Felice Andrea*. IEEE Access. 2021 [link](https://ieeexplore.ieee.org/document/9606868)
1. **Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey**. *Wenshuai Zhao, Jorge Peña Queralta, Tomi Westerlund*. IEEE Symposium Series on Computational Intelligence. 2020. [link](https://ieeexplore.ieee.org/document/9308468)


### Environments and benchmarks 
#### Robotics Environments

1. **Delving Deeper into Out-of-Distribution Detection in Deep Neural Networks**. *Alok Sahu, Harshit Pandey, et, al.* arXiv preprint arXiv:2301.04195. IEEE Robotics and Automation. 2023. [link](https://arxiv.org/abs/2301.04195)
1. **CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks**. *Oier Mees, Lukas Hermann, Erick Rosete-Beas, Wolfram Burgard.* IEEE Robotics and Automation. 2021. [link](https://arxiv.org/abs/2112.03227)
1. **robosuite: A Modular Simulation Framework and Benchmark for Robot Learning**. *Yuke Zhu, Josiah Wong, Ajay Mandlekar, Roberto Martín-Martín, Abhishek Joshi, Kevin Lin, Abhiram Maddukuri, Soroush Nasiriany, Yifeng Zhu.* IEEE Robotics and Automation. 2020. [link](https://arxiv.org/abs/2009.12293)
1. **dm_control: Software and tasks for continuous control**. *Saran Tunyasuvunakool and Alistair Muldal and Yotam Doron and Siqi Liu and Steven Bohez and Josh Merel and Tom Erez and Timothy Lillicrap and Nicolas Heess and Yuval Tassa.* Software Impacts. 2020. [link](https://www.sciencedirect.com/science/article/pii/S2665963820300099)
1. **SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation**. *Xingyu Lin, Yufei Wang, Jake Olkin, David Held* CoRL. 2020. [link](https://arxiv.org/abs/2011.07215)
1. **Assistive Gym: A Physics Simulation Framework for Assistive Robotics**. *Zackory Erickson, Vamsee Gangaram, Ariel Kapusta, C. Karen Liu, Charles C. Kemp.* International Conference on Robotics and Automation (ICRA). 2020. [link](https://arxiv.org/abs/1910.04700)
1. **Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning**. *Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Avnish Narayan, Hayden Shively, Adithya Bellathur, Karol Hausman, Chelsea Finn, Sergey Levine* CoRL. 2019. [link](https://arxiv.org/abs/1910.10897)
1. **Continuous Adaptation via Meta-Learning in Nonstationary and Competitive Environments**. *Maruan Al-Shedivat, Trapit Bansal, Yuri Burda, Ilya Sutskever, Igor Mordatch, Pieter Abbeel.* International Conference on Learning Representations. 2017. [link](https://arxiv.org/abs/1710.03641)
1. **PyBullet: Real-Time Physics Simulation**. *Erwin Coumans and Yunfei Bai.* 2017. [link](https://pybullet.org/wordpress/)
1. **OpenAI Gym**. *Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, Wojciech Zaremba.* 2016. [link](https://arxiv.org/abs/1606.01540)
1. **MuJoCo: A physics engine for model-based control**. *Emanuel Todorov, Tom Erez, Yuval Tassa.* 2012. [link](https://ieeexplore.ieee.org/document/6386109)
1. **Design and use paradigms for Gazebo, an open-source multi-robot simulator**. *Koenig, Nathan and Howard, Andrew.* 2004. [link](https://ieeexplore.ieee.org/document/1389727)

#### Robotics Benchmarks
1. **Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning**. *u, Shangding and Shi, Laixi and Wen, Muning and Jin, Ming and Mazumdar, Eric and Chi, Yuejie and Wierman, Adam and Spanos, Costas.* 2024. [link](https://github.com/SafeRL-Lab/Robust-Gymnasium)
1. **Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer**. *Xinyang Gu, Yen-Jen Wang, Jianyu Chen.* .ICRA 2024 Workshop on Agile Robotics. 2024 [link](https://arxiv.org/abs/2404.05695)
1. **NeuronsGym: A Hybrid Framework and Benchmark for Robot Tasks with Sim2Real Policy Learning**. *Haoran Li, Shasha Liu, Mingjun Ma, Guangzheng Hu, Yaran Chen, Dongbin Zhao.* IEEE Transactions on Emerging Topics in Computational Intelligence .2024. [link](https://ieeexplore.ieee.org/document/1389727)
1. **RRLS : Robust Reinforcement Learning Suite**. *Adil Zouitine, David Bertoin, Pierre Clavier, Matthieu Geist, Emmanuel Rachelson.* 2023. [link](https://arxiv.org/abs/2406.08406)
1. **ManipulaTHOR: A Framework for Visual Object Manipulation**. *Ehsani, Kiana and Han, Winson and Herrasti, Alvaro and VanderBilt, Eli and Weihs, Luca and Kolve, Eric and Kembhavi, Aniruddha and Mottaghi, Roozbeh.* CVPR. 2021. [link](https://arxiv.org/abs/2104.11213)
1. **RLBench: The Robot Learning Benchmark & Learning Environment**. *Stephen James, Zicong Ma, David Rovick Arrojo, Andrew J. Davison.* 2019. [link](https://arxiv.org/abs/1909.12271)

#### Transportation Environments
1. **TorchDriveEnv: A Reinforcement Learning Benchmark for Autonomous Driving with Reactive, Realistic, and Diverse Non-Playable Characters**. *Jonathan Wilder Lavington, Ke Zhang, Vasileios Lioutas.* 2024. [link](https://arxiv.org/abs/2405.04491)
1. **AutoVRL: A High Fidelity Autonomous Ground Vehicle Simulator for Sim-to-Real Deep Reinforcement Learning**. *Shathushan Sivashangaran, Apoorva Khairnar, Azim Eskandarian et, al.* 2023. [link](https://arxiv.org/abs/2304.11496)
1. **Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research**. *SCole Gulino, Justin Fu, Wenjie Luo, George Tucker, Eli Bronstein et, al.* 2023. [link](https://arxiv.org/abs/2310.08710)
1. **MetaDrive: Composing Diverse Driving Scenarios for Generalizable Reinforcement Learning**. *Quanyi Li, Zhenghao Peng, Lan Feng, Qihang Zhang, Zhenghai Xue, Bolei Zhou.* 2023. [link](https://arxiv.org/abs/2109.12674)

1. **InterSim: Interactive Traffic Simulation via Explicit Relation Modeling**. *Qiao Sun and Xin Huang and Brian C. Williams and Hang Zhao.* 2022. [link](https://arxiv.org/abs/2210.14413)
1. **TrafficSim: Learning to Simulate Realistic Multi-Agent Behaviors**. *Simon Suo and Sebastian Regalado and Sergio Casas and Raquel Urtasun.* 2021. [link](https://arxiv.org/abs/2101.06557)
1. **SUMMIT: A Simulator for Urban Driving in Massive Mixed Traffic**. *Panpan Cai and Yiyuan Lee and Yuanfu Luo and David Hsu.* 2020. [link](https://arxiv.org/abs/1911.04074)
1. **SMARTS: Scalable Multi-Agent Reinforcement Learning Training School for Autonomous Driving**. *Ming Zhou, Jun Luo, Julian Villella, Yaodong Yang, David Rusu, Jiayu Miao et, al.* 2020. [link](https://arxiv.org/abs/2010.09776)
1. **Deepdrive Zero**. *Craig Quiter.* 2020. [link](https://doi.org/10.5281/zenodo.3871907)
1. **CityFlow: A Multi-Agent Reinforcement Learning Environment for Large Scale City Traffic Scenario**. *{Zhang, Huichu and Feng, Siyuan and Liu, Chang and Ding, Yaoyao and Zhu et, al.* 2019. [link](http://dx.doi.org/10.1145/3308558.3314139)
1. **Highway-Env: An Environment for Autonomous Driving Decision-Making**. *Leurent, Edouard.* 2018. [link](https://github.com/eleurent/highway-env)
1. **Microscopic Traffic Simulation using SUMO**. *Lopez, Pablo Alvarez and Behrisch, Michael and Bieker-Walz, Laura and Erdmann et, al.* International Conference on Intelligent Transportation Systems (ITSC) 2018. [link](https://ieeexplore.ieee.org/document/8569938)
1. **CARLA: An open urban driving simulator**. *Dosovitskiy, Alexey and Ros, German and Codevilla, Felipe and Lopez, Antonio and Koltun, Vladlen.* CoRL 2017. [link](https://arxiv.org/abs/1711.03938)
1. **Duckietown: An open, inexpensive and flexible platform for autonomy education and research**. *Paull, Liam and Tani, Jacopo and Ahn, Heejin and Alonso-Mora, Javier and Carlone, Luca and Cap, Michal et, al.* 2017. [link](https://ieeexplore.ieee.org/document/7989179)


#### Recommender System Environments

1. **Recsim: A configurable simulation platform for recommender systems**. *Eugene Ie, Chih-wei Hsu, Martin Mladenov, Vihan Jain, Sanmit Narvekar, Jing Wang, Rui Wu, Craig Boutilier.* 2019. [link](https://arxiv.org/abs/1909.04847)
1. **Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology**. *Eugene Ie, Vihan Jain, Jing Wang, Sanmit Narvekar, Ritesh Agarwal, Rui Wu, Heng-Tze Cheng, Morgane Lustman, Vince Gatto, Paul Covington, Jim McFadden, Tushar Chandra, Craig Boutilier.* 2019. [link](https://arxiv.org/abs/1905.12767)
1. **RecoGym: A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising**. *David Rohde and Stephen Bonner and Travis Dunlop and Flavian Vasile and Alexandros Karatzoglou.* 2018. [link](https://arxiv.org/abs/1808.00720)
1. **Virtual-Taobao: Virtualizing Real-world Online Retail Environment for Reinforcement Learning**. *Jing-Cheng Shi, Yang Yu, Qing Da, Shi-Yong Chen, An-Xiang Zeng.* 2018. [link](https://arxiv.org/abs/1805.10000)

#### Recommender System Benchmarks

1. **KuaiSim: A Comprehensive Simulator for Recommender Systems**. *Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai.* 2023. [link](https://arxiv.org/abs/2309.12645)
1. **Sim-to-Real Interactive Recommendation via Off-Dynamics Reinforcement Learning**. *Wu, Junda and Xie, Zhihui and Yu, Tong and Li, Qizhi and Li, Shuai.* 2021. [link](https://offline-rl-neurips.github.io/2021/pdf/50.pdf)
1. **RL4RS: A Real-World Dataset for Reinforcement Learning based Recommender System**. *Kai Wang, Zhene Zou, Minghao Zhao, Qilin Deng, Yue Shang, Yile Liang, Runze Wu, Xudong Shen, Tangjie Lyu, Changjie Fan.* 2021. [link](https://arxiv.org/abs/2110.11073)


#### Other Environments
1. **OpenAI Gym Retro**. *OpenAI*. 2018. [link](https://openai.com/index/gym-retro/)
1. **AI2-THOR: An Interactive 3D Environment for Visual AI**. *Eric Kolve, Roozbeh Mottaghi, Winson Han, Eli VanderBilt, Luca Weihs, Alvaro Herrasti, Matt Deitke, Kiana Ehsani, Daniel Gordon, Yuke Zhu, Aniruddha Kembhavi, Abhinav Gupta, Ali Farhadi*. 2017. [link](https://arxiv.org/abs/1712.05474)
1. **DeepMind Lab**. *Charles Beattie, Joel Z. Leibo, Denis Teplyashin, Tom Ward, Marcus Wainwright, Heinrich Küttler, Andrew Lefrancq, Simon Green, Víctor Valdés, Amir Sadik, Julian Schrittwieser, Keith Anderson, Sarah York, Max Cant, Adam Cain, Adrian Bolton, Stephen Gaffney, Helen King, Demis Hassabis, Shane Legg, Stig Petersen*. 2016. [link](https://arxiv.org/abs/1612.03801)
1. **The Arcade Learning Environment: An Evaluation Platform for General Agents**. *Marc G. Bellemare, Yavar Naddaf, Joel Veness, Michael Bowling*.2013. [link](https://arxiv.org/abs/1207.4708)
#### Other Benchmarks
1. **Benchmarking Safe Exploration in Deep Reinforcement Learning**. *Alex Ray, Joshua Achiam, Dario Amodei*. 2019. [link](https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/)
1. **EnergyPlus: creating a new-generation building energy simulation program**. *Crawley, Drury B and Lawrie, Linda K and Winkelmann, Frederick C and Buhl, et, al*. 2001. [link](https://www.sciencedirect.com/science/article/abs/pii/S0378778800001146)


## Technique Papers


#### Observation

**Domain Randomization**
1. **Learning Vision-Based Bipedal Locomotion for Challenging Terrain**. *Helei Duan, Bikram Pandit, Mohitvishnu S. Gadde, Bart Van Marum, Jeremy Dao,Chanho Kim, and Alan Fern.*. IEEE International Conference on Robotics and Automation (ICRA). 2024. [link](https://arxiv.org/abs/2309.14594)
1. **Learning to Manipulate Anywhere: A Visual Generalizable Framework For Reinforcement Learning**. *Zhecheng Yuan, Tianming Wei, Shuiqi Cheng, Gu Zhang, Yuanpei Chen, Huazhe Xu*. 2024. [link](https://arxiv.org/abs/2407.15815)
1. **DROPO: Sim-to-real transfer with offline domain randomization**. *Gabriele Tiboni, Karol Arndt, Ville Kyrki
*. Robotics and Autonomous Systems. 2023. [link](https://arxiv.org/abs/2201.08434)
1. **Bridging the Reality Gap Between Virtual and Physical Environments Through Reinforcement Learning**. *Mahesh Ranaweera, Qusay H. Mahmoud et, al*. IEEE Access. 2023. [link](https://ieeexplore.ieee.org/document/10054009)
1. **Solving Rubik's Cube with a Robot Hand**. *S OpenAI et, al*. CoRR. 2019. [link](https://arxiv.org/abs/1910.07113)
1. **Asymmetric Actor Critic for Image-Based Robot Learning**. *Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, Pieter Abbeel*. CoRR. 2017. [link](https://ieeexplore.ieee.org/abstract/document/10077454)
1. **Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World**. *Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, Pieter Abbeel*. IEEE/RSJ International Conference on Intelligent Robots and Systems. 2017. [link](https://arxiv.org/abs/1703.06907)
**Domain Adaptation**

**Sensor Fusion**

**Foundation Models**

1. **xxxxxxy**. *S Rahmani, A Baghbani, et, al*. IEEE Transactions on Intelligent Transportation Systems. 2023. [link](https://ieeexplore.ieee.org/abstract/document/10077454)
1. **xxxxxxy**. *C Wu, I Kim, et, al*. 2023. [link](https://www.sciencedirect.com/science/article/pii/S1877050923005719)


#### Action
1.  **xxxxxxy**. *M Noaeen, A Naik, L Goodman, J Crebo, et, al.*. 2022. [link](https://www.sciencedirect.com/science/article/pii/S0957417422002858)
1. **xxxxxxy**. *R Chen, F Fang, N Sadeh*. 2022. [link](https://arxiv.org/abs/2206.11996)

#### Transition

1.  **xxxxxxy**. *M Noaeen, A Naik, L Goodman, J Crebo, et, al.*. 2022. [link](https://www.sciencedirect.com/science/article/pii/S0957417422002858)
1. **xxxxxxy**. *R Chen, F Fang, N Sadeh*. 2022. [link](https://arxiv.org/abs/2206.11996)

#### Reward

1.  **xxxxxxy**. *M Noaeen, A Naik, L Goodman, J Crebo, et, al.*. 2022. [link](https://www.sciencedirect.com/science/article/pii/S0957417422002858)
1. **xxxxxxy**. *R Chen, F Fang, N Sadeh*. 2022. [link](https://arxiv.org/abs/2206.11996)

<!-- 

#### IEEE Robotics and Automation
1. **Delving Deeper into Out-of-Distribution Detection in Deep Neural Networks**. *Alok Sahu, Harshit Pandey, et, al.* arXiv preprint arXiv:2301.04195. 2023. [link](https://arxiv.org/abs/2301.04195)
1. **CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks**. *Oier Mees, Lukas Hermann, Erick Rosete-Beas, Wolfram Burgard.* arXiv preprint arXiv:2112.03227. 2021. [link](https://arxiv.org/abs/2112.03227)
1. **robosuite: A Modular Simulation Framework and Benchmark for Robot Learning**. *Yuke Zhu, Josiah Wong, Ajay Mandlekar, Roberto Martín-Martín, Abhishek Joshi, Kevin Lin, Abhiram Maddukuri, Soroush Nasiriany, Yifeng Zhu.* 2020. [link](https://arxiv.org/abs/2009.12293)
#### Software Impacts
1. **dm_control: Software and tasks for continuous control**. *Saran Tunyasuvunakool and Alistair Muldal and Yotam Doron and Siqi Liu and Steven Bohez and Josh Merel and Tom Erez and Timothy Lillicrap and Nicolas Heess and Yuval Tassa.* 2020. [link](https://www.sciencedirect.com/science/article/pii/S2665963820300099)
#### CoRL
1. **SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation**. *Xingyu Lin, Yufei Wang, Jake Olkin, David Held* CoRL. 2020. [link](https://arxiv.org/abs/2011.07215)
1. **Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning**. *Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Avnish Narayan, Hayden Shively, Adithya Bellathur, Karol Hausman, Chelsea Finn, Sergey Levine* CoRL. 2019. [link](https://arxiv.org/abs/1910.10897)
#### International Conference on Robotics and Automation (ICRA)
1. **Assistive Gym: A Physics Simulation Framework for Assistive Robotics**. *Zackory Erickson, Vamsee Gangaram, Ariel Kapusta, C. Karen Liu, Charles C. Kemp.* International Conference on Robotics and Automation (ICRA). 2020. [link](https://arxiv.org/abs/1910.04700)
#### International Conference on Learning Representations
1. **Continuous Adaptation via Meta-Learning in Nonstationary and Competitive Environments**. *Maruan Al-Shedivat, Trapit Bansal, Yuri Burda, Ilya Sutskever, Igor Mordatch, Pieter Abbeel.* International Conference on Learning Representations. 2017. [link](https://arxiv.org/abs/1710.03641)
#### Others
1. **PyBullet: Real-Time Physics Simulation**. *Erwin Coumans and Yunfei Bai.* 2017. [link](https://pybullet.org/wordpress/)
1. **OpenAI Gym**. *Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, Wojciech Zaremba.* 2016. [link](https://arxiv.org/abs/1606.01540)
### Sim-to-Real Benchmarks

## Transportation
### Environment
### Sim-to-Real Benchmark
## Recommender Systems
### Environment
### Sim-to-Real Benchmark
## Others
### Environment
### Sim-to-Real Benchmark -->


# Cite

If you find AwesomeSim2real and our survey paper useful for your research or development, please cite our [paper](xxxxxxx).

```
@article{xxx,
  title={xxx: xxx},
  author={xxxx},
  journal={arXiv preprint arXiv:xxx},
  year={2025}
}
```
