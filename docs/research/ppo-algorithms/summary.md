# Proximal Policy Optimization (PPO) - Podsumowanie

Proximal Policy Optimization (PPO) to popularny i efektywny algorytm uczenia ze wzmocnieniem (ang. reinforcement learning, RL), wprowadzony przez OpenAI jako ulepszenie starszych metod gradientu polityki, takich jak Trust Region Policy Optimization (TRPO). PPO znajduje równowagę między wydajnością a efektywnością obliczeniową, co czyni go odpowiednim wyborem do szerokiego zakresu zadań RL.

## 1. Podstawy teoretyczne

PPO należy do rodziny algorytmów gradientu polityki, które uczą się bezpośrednio polityki (funkcji decyzyjnej) agenta. W PPO kluczowym celem jest optymalizacja funkcji nagrody przy jednoczesnym utrzymaniu stabilności treningu i unikania dużych zmian w polityce, co mogłoby prowadzić do niestabilności. 

Aby to osiągnąć, PPO wprowadza ograniczenie na to, jak bardzo polityka może się zmieniać między aktualizacjami. Wykorzystuje tzw. *klipowane* funkcje celu, aby zapobiec zbyt dużym zmianom polityki w jednym kroku aktualizacji. Dzięki temu PPO jest prostsze i bardziej wydajne w implementacji w porównaniu do innych algorytmów, takich jak TRPO, które wymagają bardziej skomplikowanych obliczeń.

## 2. Mechanizmy PPO

PPO działa poprzez:

- **Użycie funkcji celu (objective function)**: PPO maksymalizuje funkcję nagrody przy jednoczesnym zastosowaniu ograniczenia (*clip*) na stosunek prawdopodobieństw między starą a nową polityką, aby uniknąć dużych, destrukcyjnych zmian.
- **Wykorzystanie wielu kroków aktualizacji**: PPO wykorzystuje mini-batche próbek do efektywnego obliczania aktualizacji gradientu, co pozwala na bardziej stabilne i efektywne uczenie.
- **Stosowanie *Advantage Estimation***: PPO często korzysta z GAE (Generalized Advantage Estimation), co pozwala na bardziej precyzyjne i stabilne szacowanie korzyści, które agent osiąga w danej sytuacji.

## 3. Dlaczego PPO?

PPO zostało wybrane ze względu na jego zalety:

- **Stabilność treningu**: PPO ogranicza zmiany w polityce, co zmniejsza ryzyko niestabilności, często obserwowane w innych metodach gradientu polityki.
- **Prostota implementacji**: PPO, w przeciwieństwie do TRPO, jest prostsze do implementacji, co przekłada się na łatwiejszą integrację i optymalizację w projekcie.
- **Efektywność obliczeniowa**: Algorytm ten nie wymaga kosztownych obliczeń, jak np. obliczanie hessianu (drugiej pochodnej), co sprawia, że jest wydajny i szybki.

## 4. Dalsza lektura

Aby zgłębić szczegóły teoretyczne i implementacyjne PPO, polecamy następujące źródła:

- [OpenAI Baselines: PPO](https://openai.com/blog/openai-baselines-ppo/)
- Schulman et al., "Proximal Policy Optimization Algorithms" (2017) - [Link do publikacji](https://arxiv.org/abs/1707.06347)
- Sutton & Barto, "Reinforcement Learning: An Introduction" (2018) - Podstawowy podręcznik dotyczący teorii uczenia ze wzmocnieniem.

Warto obejrzeć/przeczytać:
-https://openai.com/index/openai-baselines-ppo/
-https://www.youtube.com/watch?v=5P7I-xPq8u8

PPO to algorytm, który znajduje szerokie zastosowanie w wielu projektach RL, dzięki czemu jest idealnym wyborem do naszych celów, zapewniając stabilność, wydajność i łatwość implementacji.
