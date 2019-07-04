1. Do poprawnego uruchomienia gry, wymagany jest Python3 oraz modu³ Pygame
   Mo¿na go zainstalowaæ, za pomoc¹ nastêpuj¹cego polecenia:
	python pip -m install pygame
   Wczeœniej warto zaktualizowaæ wersjê pip, za pomoc¹ polecenia:
	python pip -m install --upgrade pip
   UWAGA: Wymagane s¹ uprawnienia administratora (lub odpowiednio roota)

2. Grê mo¿na uruchomiæ z lini komend:
	python3 Pong.py
   Lub klikaj¹c na ikonkê dwukrotnie (pod warunkiem, ¿e skonfigorowano domyœlne otwieranie za pomoc¹ Python 3)

3. Domyœlne ustawienia gry:
	a) Rozmiar okienka 800x600
	b) Gra pomiêdzy dwójk¹ graczy
	c) Gracz pierwszy steruje za pomoc¹ strza³ek (góra/dó³) lub przycisków w/s
	d) Gracz drugi steruje za pomoc¹ myszki (wyskoœæ paletki == wysokoœæ myszki na okienku gry)

4. Dostêpne s¹ nastêpuj¹ce modyfikacje:
	a) Rozmiar okienka mo¿na okreœliæ zapisuj¹c go w pliku config.txt
	   UWAGA:
		- Jeœli zdefiniowana w pliku config.txt szerokoœæ bêdzie mniejsza ni¿ 800,
		  lub wysokoœæ bêdzie mniejsza ni¿ 600, to okienku zostanie nadany domyœlny rozmiar
		- Plik config.txt musi znajdowaæ siê w tym samym katalogu co gra
		- Parametry podajemy po przecinku: najpierw szerokoœæ, nastêpnie d³ugoœæ okienka
	b) Aby wyjœæ, klikamy przycisk "Esc"
	c) Aby zapauzowaæ, klikamy przycisk "p"
	d) Aby wznowiæ grê, klikamy spacjê
	e) Mo¿na sterowaæ prêdkoœci¹ pi³ki za pomoc¹ przcików 1-9
	f) Mo¿na zamieniæ gracza pierwszego na komputer, w tym celu klikamy przycisk "TAB"
	g) Mo¿na sterowaæ poziomem trudnoœci komputera, w tym celu naciskamy:
		- "x", dla poziomu ³atwego
		- "y", dla poziomu œredniego
		- "z", dla poziomu trudnego
	h) Aby powróciæ do manualnego sterowania drugim graczem, wciskamy przycisk "q"
	i) Aby zresetowaæ wyœwietlany wynik, klikamy przycisk "r"

5. Dodatkowe uwagi:
	a) Gracz pierwszy ma kolor czerwony, natomiast drugi niebieski.
	b) Poziom trudnoœci gry z komputerem jest bezpoœrenio powi¹zany z szybkoœci¹ pi³ki.
	   Im pi³ka porusza siê szybciej, tym wiêksze szanse na pomy³kê bota.
	c) Po zapauzowaniu jedynym aktywnym klawiszem staje siê spacja, która wznawia grê.
	d) Zalecana proporcja okienka to 4:3
	e) Pi³ka odbija siê zawsze o 90 stopni.
	   Jednym wyj¹tkiem od tej regu³y, jest uderzenie pi³ki rogiem paletki.
	   Wówczas pi³ka odbija siê o 180 stopni.