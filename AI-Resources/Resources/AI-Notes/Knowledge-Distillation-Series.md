# Knowledge Distillation Family

## Papers

| Topic | Year | Conference |
| --- | --- | --- |
| [Distilling the Knowledge in a Neural Network (Knowledge Distillation)](https://arxiv.org/abs/1503.02531) | 2015 |  |
| [On the Efficacy of Knowledge Distillation](https://openaccess.thecvf.com/content_ICCV_2019/papers/Cho_On_the_Efficacy_of_Knowledge_Distillation_ICCV_2019_paper.pdf) | 2019 |  |  |
| [Does Knowledge Distillation Really Work?](https://openreview.net/pdf?id=7J-fKoXiReA) | 2021 |  |  |

# Distilling the Knowledge in a Neural Network

## Knowledge Distillation Details

<img src="figures/knowledge-distillation/knowledge_distillation_1.png" width=80% height=80%>

## Training Objectives

<img src="figures/knowledge-distillation/knowledge_distillation_2.png" width=80% height=80%>

## Experiment Details

<img src="figures/knowledge-distillation/knowledge_distillation_3.png" width=80% height=80%>


<br>
<hr>
<br>

# On the Efficacy of Knowledge Distillation

Bigger models with more accuracy does not mean they are good teachers. Early stopped teachers are better.

## Knowledge Distillation Diagram

<img src="figures/knowledge-distillation/knowledge_distillation_efficacy_1.png" width=50% height=50%>

## Knowledge Distillation Loss Function

<img src="figures/knowledge-distillation/knowledge_distillation_efficacy_3.png" width=50% height=50%>

## Abstract and Model Simplification

<img src="figures/knowledge-distillation/knowledge_distillation_efficacy_2.png" width=50% height=50%>

<!--
<img src="figures/knowledge-distillation/knowledge_distillation_efficacy_4.png" width=90% height=90%>
-->

## Knowledge Distillation Gets Worse Than Scratch

<img src="figures/knowledge-distillation/knowledge_distillation_efficacy_5.png" width=50% height=50%>

## Early Teacher Training Stopping

<img src="figures/knowledge-distillation/knowledge_distillation_efficacy_6.png" width=50% height=50%>

<br>
<hr>
<br>

# Does Knowledge Distillation Really Work?

Optimization is a key reason for student not matching teacher and matching teacher does not mean better student generalization. `Fidelity` students ability to match teacher predictions, `generalization` performance on unseen data.

<img src="figures/knowledge-distillation/distillation_really_work_1.png" width=80% height=80%>

<img src="figures/knowledge-distillation/distillation_really_work_2.png" width=80% height=80%>
