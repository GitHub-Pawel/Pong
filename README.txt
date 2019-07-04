1. Do poprawnego uruchomienia gry, wymagany jest Python3 oraz modu� Pygame
   Mo�na go zainstalowa�, za pomoc� nast�puj�cego polecenia:
	python pip -m install pygame
   Wcze�niej warto zaktualizowa� wersj� pip, za pomoc� polecenia:
	python pip -m install --upgrade pip
   UWAGA: Wymagane s� uprawnienia administratora (lub odpowiednio roota)

2. Gr� mo�na uruchomi� z lini komend:
	python3 Pong.py
   Lub klikaj�c na ikonk� dwukrotnie (pod warunkiem, �e skonfigorowano domy�lne otwieranie za pomoc� Python 3)

3. Domy�lne ustawienia gry:
	a) Rozmiar okienka 800x600
	b) Gra pomi�dzy dw�jk� graczy
	c) Gracz pierwszy steruje za pomoc� strza�ek (g�ra/d�) lub przycisk�w w/s
	d) Gracz drugi steruje za pomoc� myszki (wysko�� paletki == wysoko�� myszki na okienku gry)

4. Dost�pne s� nast�puj�ce modyfikacje:
	a) Rozmiar okienka mo�na okre�li� zapisuj�c go w pliku config.txt
	   UWAGA:
		- Je�li zdefiniowana w pliku config.txt szeroko�� b�dzie mniejsza ni� 800,
		  lub wysoko�� b�dzie mniejsza ni� 600, to okienku zostanie nadany domy�lny rozmiar
		- Plik config.txt musi znajdowa� si� w tym samym katalogu co gra
		- Parametry podajemy po przecinku: najpierw szeroko��, nast�pnie d�ugo�� okienka
	b) Aby wyj��, klikamy przycisk "Esc"
	c) Aby zapauzowa�, klikamy przycisk "p"
	d) Aby wznowi� gr�, klikamy spacj�
	e) Mo�na sterowa� pr�dko�ci� pi�ki za pomoc� przcik�w 1-9
	f) Mo�na zamieni� gracza pierwszego na komputer, w tym celu klikamy przycisk "TAB"
	g) Mo�na sterowa� poziomem trudno�ci komputera, w tym celu naciskamy:
		- "x", dla poziomu �atwego
		- "y", dla poziomu �redniego
		- "z", dla poziomu trudnego
	h) Aby powr�ci� do manualnego sterowania drugim graczem, wciskamy przycisk "q"
	i) Aby zresetowa� wy�wietlany wynik, klikamy przycisk "r"

5. Dodatkowe uwagi:
	a) Gracz pierwszy ma kolor czerwony, natomiast drugi niebieski.
	b) Poziom trudno�ci gry z komputerem jest bezpo�renio powi�zany z szybko�ci� pi�ki.
	   Im pi�ka porusza si� szybciej, tym wi�ksze szanse na pomy�k� bota.
	c) Po zapauzowaniu jedynym aktywnym klawiszem staje si� spacja, kt�ra wznawia gr�.
	d) Zalecana proporcja okienka to 4:3
	e) Pi�ka odbija si� zawsze o 90 stopni.
	   Jednym wyj�tkiem od tej regu�y, jest uderzenie pi�ki rogiem paletki.
	   W�wczas pi�ka odbija si� o 180 stopni.