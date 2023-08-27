the task
Ciąg składający się z nawiasów otwierających i zamykających nazwiemy nawiasowaniem. Nawiasowanie jest
poprawne, jeśli nawiasy można tak połączyć w pary, żeby były poprawnie zagnieżdżone. Definiujemy też głębokość zagnieżdżenia.
Formalnie poprawne nawiasowanie można zdefiniować rekurencyjnie:
• Ciąg pusty jest poprawnym nawiasowaniem; jego głębokość wynosi 0.
• Jeśli ciąg w jest poprawnym nawiasowaniem o głębokości h, to ciąg (w), który powstaje przez dopisanie
nawiasu otwierającego na początku i nawiasu zamykającego na końcu, jest poprawnym nawiasowaniem
o głębokości h + 1.
• Jeśli ciągi w1 i w2 są poprawnymi nawiasowaniami o głębokościach, odpowiednio, h1 i h2, to ciąg w1w2,
który powstaje przez ich sklejenie, jest poprawnym nawiasowaniem o głębokości max(h1, h2).
Dane są poprawne nawiasowanie w i liczba H. Przez odwrócenie nawiasu rozumiemy zmianę pewnego
nawiasu otwierającego na zamykający lub odwrotnie. Ile minimalnie odwróceń nawiasów trzeba wykonać,
żeby uzyskać poprawne nawiasowanie o głębokości nie większej niż H?
Wejście
W pierwszym wierszu wejścia znajdują się dwie liczby całkowite n i H (n ≥ 2, 1 ≤ H ≤
n
2
) oznaczające długość
ciągu oraz maksymalną głębokość.
W drugim wierszu znajduje się n-literowy napis składający się ze znaków ( i ), będący poprawnym nawiasowaniem.
Wyjście
Twój program powinien wypisać jedną liczbę całkowitą oznaczającą minimalną liczbę odwróceń nawiasów,
jakie trzeba wykonać, aby uzyskać poprawne nawiasowanie o głębokości co najwyżej H.
Przykład
Dla danych wejściowych:
8 2
(()(()))
poprawnym wynikiem jest:
2
Wyjaśnienie przykładu: Ciąg (()(())) ma głębokość 3. Odwrócenie piątego i szóstego nawiasu da nam
ciąg (()()()) o głębokości 2.
Jedno odwrócenie nawiasu nie wystarczy, bo nie uzyskamy w ten sposób poprawnego nawiasowania.
Testy „ocen”:
1ocen: n = 20, w = (((((((((()))))))))), H = 10; odpowiedź to 0;
2ocen: n = 20, w = (((((((((()))))))))), H = 1; odpowiedź to 10;
3ocen: n = 1 000 000, w = (
n
2 )
n
2 , H = 1; odpowiedź to n
2