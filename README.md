# Proiect 10 – Simulări și Modele Agent-Based în Python

Acest repository conține zece aplicații scrise în Python, fiecare demonstrând concepte cheie din simularea proceselor stocastice și modele agent-based.

## 1. Simulare coadă simplă cu SimPy

Programul generează clienți care sosesc la intervale aleatoare și sunt deserviți de un singur server. Se folosesc:
- modulele simpy și random
- o coadă cu capacitate 1
- afișarea timpului de servire

## 2. Model logistic de evoluție a populației

Se utilizează scipy.integrate.solve_ivp pentru a simula evoluția unei populații între anii 1925 și 2025, după ecuația logistică. Codul include:
- funcție de evoluție cu coeficienți de creștere și limitare
- generare grafică cu matplotlib

## 3. Sumă cumulativă a aruncărilor cu zarul

Se simulează 50 de aruncări cu un zar de 12 fețe folosind numpy, apoi:
- se calculează suma cumulativă
- se afișează primele 5 rezultate

## 4. Simulare autoregresivă a temperaturii anuale

Se generează un șir de temperaturi pe 50 de ani folosind:
- model autoregresiv cu coeficient
- distribuție normală pentru zgomotul aleator

## 5. Simulare distribuție normală a timpilor participanților

Se simulează timpii de finalizare pentru 50 de participanți la un concurs, conform unei distribuții normale:
- medie dată și deviație standard
- afișarea primilor 5 timpi generați

## 6. Simulare coadă cu distribuție exponențială

Programul folosește simpy și numpy pentru a simula procesarea a 10 cereri. Caracteristici:
- timpi de sosire și servire generați exponențial
- procesarea printr-un server unic

## 7. Simulare coadă cu timp de servire randomizat

Se creează o simulare în care 5 clienți sosesc și sunt serviți:
- timpi de servire generați aleator (exponențial)
- afișarea sosirii și plecării fiecărui client

## 8. Model simplu agent-based cu lucrători și angajatori

Se definește o clasă Agent și un mediu cu o grilă 2D. Caracteristici:
- adăugarea și mutarea agenților
- clase derivate pentru lucrători și angajatori
- modelul JobMarket

## 9. Simulare firmă–piață cu ajustări de preț

Se modelează un mediu economic în care firmele:
- au cote de piață diferite
- își ajustează prețurile în funcție de cerere
- se folosește o grilă și o clasă Market

## 10. Model trafic rutier cu Mesa

Se creează o simulare complexă de trafic cu biblioteca mesa. Include:
- agenți de tip Car și Intersection
- reacții la semafoare în funcție de densitate
- colectare de date și grafic al vitezei medii
- calcul al densității la intersecții
