%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                     %
% Readme zur Verwendung des Paketes themeKonstanz     %
% zur Erstellung von PDF-Dokumenten und Abschluss-    %
% arbeiten im neuen Corporate Design der Universität  %
% Konstanz                                            %
%                                                     %
% Stand: 14.09.2016 - Michael Brendle (Version 0.4)   %
%                                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


Struktur des Verzeichnisses:

README.txt                            -- diese Datei
themeKonstanz.sty                     -- Paket mit allen Definitionen, Makros und
                                         Umgebungen
themeKonstanzStyleAddOn.sty           -- Style Add-On für ein zusätzliches Design
                                         für Kapitel und diverse Abschnitss-
                                         überschriften, jedoch nicht im Corporate
                                         Design der Universität Konstanz. Dies
                                         soll eine Alternative für Abschlussarbeiten
                                         sein.
themeKonstanzXelatexAddOn.sty         -- XeLaTeX Add-On, welches beim Übersetzen
                                         mit XeLaTeX geladen werden muss um die
                                         Systemschriftart Arial zu verwenden.
beispielPDF.tex                       -- Beispiel eins PDF-Dokumentes im
                                         Corporate Design der Universität Konstanz
beispielPDF.pdf                       -- übersetzte PDF dieses PDF Dokumentes
beispielThesis.tex                    -- Beispiel einer Abschlussarbeit im Corporate
                                         Design der Universität Konstanz mit
                                         Deckblatt des Fachbereichs Informatik
                                         und Informationswissenschaft
beispielThesis.pdf                    -- übersetzte PDF dieser Abschlussarbeit
graphics/                             -- Ordner mit Graphiken



Diese Readme ist in die folgenden Abschnitte untergliedert:

1.  Übersetzen der Tex-Datei
2.  Dokumentenklasse
3.  Einbinden des Hauptpaketes
4.  Einbinden der Add-Ons
5.  Auswahl des Papierformates
6.  Dokumentinformationen
7.  Kopf- und Fusszeile
8.  Erzeugen eines Textfelds
9.  Uni-Titelseite
10. Thesis-Titelseite
11. Inhalts-, Tabellen- und Abbildungsverzeichnis
12. Kapitel und Abschnitte
13. Aufzählung
14. Abbildungen
15. Tabellen
16. Farben des Corporate Design
17. Auswahl der Schriftgröße
18. CD Element: Markieren
19. CD Element: Unterstreichen
20. CD Element: Merken
21. CD Element: Block
22. CD Element: Linie (mit optionalen Pfeilen)
23. CD Element: Klammer (mit optionalen Pfeilen)
24. Literaturverzeichnis
25. Sonstiges



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 1. Übersetzen der Tex-Datei  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Die Tex-Datei kann ganz normal mittels PDFLatex oder bei
Verwendung des XeLaTeX-Add-Ons mit XeLaTeX übersetzt werden.

Der Vorteil bei der Überstzung mittels XeLaTeX ist es, dass
die Systemschriftart Arial verwendet werden kann, welches nach
Corporate Design Richtlinien verwendet werden soll. Jedoch erreicht
man mit der serifenlosen Schrift und PDFLatex ein fast genauso gutes
Ergebnis.

XeLaTeX wird bereits in den meisten TeX-Distributionen mitgeliefert.
Sollte es nicht mitgeliefert sein, kann es problemlos nachinstalliert
werden.

Für das Erstellen der Elemente des Corporate Design werden einige
weitere Pakete benötigt. In der folgenden Liste sind die notwendigen
Pakete aufgelistet, die nicht überall standardmäßig vorinstalliert sind:

- xcolor
- textpos
- xunicode
- soul
- tikz
- ifthen
- keycommand
- calc
- float
- cmbright
- fontspec
- caption
- chngcntr
- tabu
- fixltx2e (ab Tex-Version 2015 nicht mehr notwendig)
- fancyhdr
- titlesec

Zudem kann es sein, dass diese Pakete weitere Pakete voraussetzen. Diese
müssen dann ebenfalls installiert werden. Der Compiler wird für diesen Fall
die Pakete anzeigen, welche zusätzlich noch benötigt werden.

Des Weiteren ist es wichtig, dass alle Pakete, sowie ihre Tex-Distribution
auf dem aktuellen Stand sind, um mögliche Probleme aus dem Weg zu gehen.

Sollten Sie Probleme beim Kompilieren haben, können Sie dieses Dokument auch
online, in Overleaf, unter der URL

 https://www.overleaf.com/6205861nhvynn

einsehen, bearbeiten und übersetzen.

Generell stellt Overleaf eine weitere gute Variante dar dieses Dokument
zu übersetzen, da sie sich dann nicht über den aktuellen Stand ihrer
Tex-Distribution, sowie Pakete kümmern müssen.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 2. Dokumentenklasse          %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Als Dokumentenklasse wird die KOMA-Skript 'report' Klasse verwendet.

Als Standardchriftgröße wird 11pt verwendet.

Zudem muss die Option rgb eingeschalten werden, damit die definierten
Farben des HSB Farbraums in den RGB Farbraum umgewandelt werden, da
einige Pakete keinen HSB Farbraum unterstützen.

> \documentclass[11pt, rgb]{scrreprt}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3. Einbinden des Hauptpaketes %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Alle verwendeten Makros und Umgebeungen, die zur Erstellung von
PDF-Dokumenten und Abschlussarbeiten benötigt werden, können
aus dem Paket themeKonstanz geladen werden, welches sich in der
Datei themeKonstanz.sty befindet.

Das Paket wird mittels folgendem Befehl importiert:

> \usepackage{themeKonstanz}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 4. Einbinden der Add-Ons      %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Neben dem Hauptpaket, welches immer eingebunden werden muss, stehen
zwei Add-Ons zur Verfügung:

- XeLaTeX Add-On
- Style Add-On

Möchte man dieses Dokument mit XeLaTeX anstatt PDFLatex kompilieren,
um die Systemschrift Arial zu verwenden, dann muss zusätzlich das
Add-On Paket themeKonstanzXelatexAddOn, welches sich in der Datei
themeKonstanzXelatexAddOn.sty befindet *VOR* dem eigentlichen
Paket themeKonstanz geladen werden:

> \usepackage{themeKonstanzXelatexAddOn} % XeLaTeX mit Schriftart Arial,
> %                                        VOR dem Standardpaket importieren

Möchte man ein Style Add-On verwenden, das aus meiner
Bachelorarbeit aus dem Jahr 2015 stammt, so muss *NACH* dem Laden
des Paketes themeKonstanz dieses zusätzliche Paket
themeKonstanzStyleAddOn, welches sich in der Datei
themeKonstanzStyleAddOn.sty befindet, geladen werden. Dabei
werden die Überschriften der Kapitel, der Abschnitte, der Unter-
Abschnitte und des Unterunterabschnittes geändert. Dieses
Add-On wird vor allem für Abschlussarbeiten empfohlen, die
nicht zu farbig sein sollten und nicht so strikt an das
Corporate Design der Universität Konstanz gebunden sind.

> \usepackage{themeKonstanzStyleAddOn} % Style Add-On für andere Überschriften,
> %                                      NACH dem Standardpaket importieren



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 5. Auswahl des Papierformates %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$

Mit Hilfe des Makros

    \format{<key>}

kann das Papierformat angepasst werden.

Zur Auswahl stehen folgende Papierformate:

   Schlüssel  Beschreibung      Höhe      Breite
   -----------------------------------------------
   a3         DinA3 Hochformat  42.0  cm  29.7  cm
   a3quer     DinA3 Querformat  29.7  cm  42.0  cm
   a4         DinA4 Hochformat  29.7  cm  21.0  cm
   a4quer     DinA4 Querformat  21.0  cm  29.7  cm
   a5         DinA5 Hochformat  21.0  cm  14.8  cm
   a5quer     DinA5 Querformat  14.8  cm  21.0  cm

Falls keiner der unterstützten Schlüssel übergeben wird,
ist DinA4 Hochformat der Standard.

Somit würde der folgende Befehl das Papierformat DinA4 Hochformat auswählen:

> \format{a4}




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 6. Dokumentinformationen       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Für das Dokument können mit Hilfe der Makros

    \date{...}
    \year{...}
    \author{...}
    \title{...}
    \subtitle{...}
    \unisection{...}
    \department{...}
    \supervisorOne{...}
    \supervisorTwo{...}

das Datum, das Jahr, der Autor / die Autoren, der Titel, der
Unteritel des Dokumentes, die Sektion an der Universität,
der Fachbereich an der Universität, der Erstgutachter und der
Zweitgutachter bestimmt werden.

Je nachdem, ob die Corporate Design Titelseite oder die
Thesis-Titelseite ausgewählt wird, werden die entsprechenden
Angaben dargestellt und verwendet. Außerdem benutzen die
Kopf- und Fusszeile diese Informationen (siehe weiter unten).

> \date{14.09.2016}
> \year{2016}
> \author{Autor des Dokuments}
> \title{Beispiel-PDF im Corporate Design der Universität Konstanz}
> \subtitle{Untertitel des Dokuments}
> \unisection{Mathematisch-Naturwissenschaftlichen Sektion}
> \department{Fachbereich Informatik und Informationswissenschaft}
> \supervisorOne{Prof. Dr. tba}
> \supervisorTwo{Prof. Dr. tba}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 7. Kopf- und Fusszeile       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Mit Hilfe des Makros

    \headFoot

kann aus 20 vordefinierten Kopf- und Fusszeilen
gewählt werden.

Dieses Makro besitzt ein Argument, nämlich die
ID aus den 20 vordefinierten Kopf- und Fusszeilen:

    \headFoot{<ID>}

Bei den IDs 1, 2, 5, 6, 9, 10, 13, 14, 17 und 18
mit | wird auf ungerade und gerade Seite geachtet.

Bei den restlichen IDs ist die Kopf- und Fusszeile auf
ungeraden und geraden Seiten gleich.

Dies soll vor allem dem Benutzer die Entscheidung
überlassen, ob er das Dokument einseitig oder doppelseitig
ausdruckt.


   ID    Beschreibung
   ------------------
   1     Kopfzeile: Seite --- Kapitel --- Autor | Autor --- Kapitel --- Seite
         Fusszeile:

   2     Kopfzeile:
         Fusszeile: Seite --- Kapitel --- Autor | Autor --- Kapitel --- Seite

   3     Kopfzeile: Autor --- Kapitel --- Seite
         Fusszeile:

   4     Kopfzeile:
         Fusszeile: Autor --- Kapitel --- Seite

   5     Kopfzeile: Seite --- Autor --- Kapitel | Kapitel --- Autor --- Seite
         Fusszeile:

   6     Kopfzeile:
         Fusszeile: Seite --- Autor --- Kapitel | Kapitel --- Autor --- Seite

   7     Kopfzeile: Kapitel --- Autor --- Seite
         Fusszeile:

   8     Kopfzeile:
         Fusszeile: Kapitel --- Autor --- Seite

   9     Kopfzeile: Seite --- --- Kapitel | Name --- --- Seite
         Fusszeile:

   10    Kopfzeile:
         Fusszeile: Seite --- --- Kapitel | Name --- --- Seite

   11    Kopfzeile: Kapitel --- --- Seite
         Fusszeile:

   12    Kopfzeile:
         Fusszeile: Kapitel --- --- Seite

   13    Kopfzeile: Seite --- --- Autor | Kapitel --- --- Seite
         Fusszeile:

   14    Kopfzeile:
         Fusszeile: Seite --- --- Autor | Kapitel --- --- Seite

   15    Kopfzeile: Autor --- --- Seite
         Fusszeile:

   16    Kopfzeile:
         Fusszeile: Autor --- --- Seite

   17    Kopfzeile: Seite --- --- | --- --- Seite
         Fusszeile:

   18    Kopfzeile:
         Fusszeile: Seite --- --- | --- --- Seite

   19    Kopfzeile: --- --- Seite
         Fusszeile:

   20    Kopfzeile:
         Fusszeile: --- --- Seite

 Weitere individuelle Kopf- und Fusszeilen können in der .sty Datei angepasst
 werden.

> \headFoot{14}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 8. Erzeugen eines Textfeldes %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Damit ein problemloses Anordnen der Elemente auf einer Seite möglich ist,
steht ein neue Umgebeung mit dem Namen

    textfeld

zur Verfügung.

Diese Umgebung besteht aus zwei unbedingt notwendigen Argumenten und einem
optionalen Argument.

> \begin{textfeld}[optionales Argument]{1. Argument}{2. Argument}
>     ...
> \end{textfeld}

Innerhalb der Umgebung kann dann der Inhalt des Textfeldes hinterlegt werden.

Die Argumente haben dabei folgende Bedeutung:

  Optionales Argument: Hier wird die Breite des Textfeldes festgelegt.
                       Wird dies Weggelassen wird einfach die Papierbreite
                       als Breite des Textfeldes angegeben. Dies kann nützlich sein
                       wenn man nicht weiß, wie breit der Inhalt werden kann.
                       Dringend verwenden sollte man dieses Argument, wenn man
                       beispielsweise Textumbrüche erzeugen will anhand der vorgegebenen
                       Breite.

  1. Argument:         Hier wird die x-Koordinate der linken oberen Ecke des Textfeldes
                       angegeben.

  2. Argument:         Hier wird die y-Koordinate der linken oberen Ecke des Textfeldes
                       angegeben.

Für die beiden Argumente, ist noch wichtig zu wissen, wie die Koordinaten verstanden
werden sollten:

               x-Achse

               0                         \paperwidth
          y  0 -------------------------------------
          -    |                                   |
          A    |                                   |
          c    |                                   |
          h    |                                   |
          s    |                                   |
          e    |                                   |
               |                                   |
               |               ...                 |
               |                                   |
               |                                   |
               |                                   |
               |                                   |
               |                                   |
               |                                   |
               |                                   |
               |                                   |
  \paperheight -------------------------------------

  - Dabei handelt es sich überall um positive Werte und um absolute Koordinaten.

  - Zudem muss immer die jeweilige Einheit an den Wert hinzuegfügt werden, damit der
    Wert richtig interpretiert werden kann. Möchte man vorher beispielsweise eine Skizze
    machen, dann empfiehlt es sich hier cm als Einheit zu verwenden.

  - Mittles \paperwidth und \paperheight können auch Koordinaten angegeben werden,
    die relativ zum Papierformat sind. Durch das calc Paket ist es zudem möglich
    Rechnungen innerhalb der Argumente vorzunehmen.

    Möchte man beispielsweise fünf Zentimeter sowohl vom linken als auch unteren Ende
    ein Textfeld beginnen, so würde der Befehl wie folgt aussehen:

> \begin{textfeld}{\paperwidth - 5cm}{\paperheight - 5cm}
>     ...
> \end{textfeld}


Zudem sollte man noch wissen, dass alle neueren Textfelder, also jene die weiter unten
stehen, die älteren überdecken. Dadurch sollte das Plakat von hinten nach vorne aufgebaut
werden.


Der folgende Befehlt fügt nun an der Koordinate (3 cm, 7 cm) das folgende Textfeld hinzu,
welches als Inhalt ein (Hintergrund)bild besitzt, mit einer Breite von
Papierbreite - 3 cm. Somit geht das übergeben Bild bis an den rechten Rand heran.

\begin{textfeld}{3cm}{7cm}%
\includegraphics[width=\paperwidth - 3cm]{graphics/luftaufnahme_sw.png}%
\end{textfeld}%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 9. Uni-Titelseite            %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Mit Hilfe des Makros

    \unititlepage

kann die Titleseite des Dokumentes im Corporate Design der
Universität Konstanz erstellt werden.

Das Makro besitzt drei optionale Argumente, die mit
Key-Value-Pairs eingesetzt werden können:

    \unititlepage[Optionen mit Key-Value-Pairs]

Dabei stehen folgende Optionen zur Verfügung:

    graphic      Möchte man ein Bild, Grafik, o.ä. auf der
                 Titelseite platzieren, so muss nur der Pfad
                 dieser Grafik eingesetzt werden (Beispiel siehe
                 unten).

                 Wird kein Grafikpfad angegeben oder wird dieses
                 optionale Argument weggelassen, so wird ein
                 leeres graues Rechteck entsprechend CD-Richtlinien
                 erstellt.

    partnerlogo  Möchte man ein Partner- bzw. Zweitlogo auf der
                 Titelseite platzieren, so muss auch hier der
                 Pfad angegeben werden, und es wird in der linken
                 oberen Ecke platziert (Beispiel siehe unten).

                 Wird dieses optionale Argument weggelassen, so wird
                 an dieser Stelle natürlich kein Logo präsentiert.

    unilogo      Standardmäßig wird in der rechten oberen Ecke auf
                 der Titelseite das Unilogo platziert.

                 Möchte man an dieser Stelle ein anderes Logo, so muss
                 auch hier der Pfad angegeben werden. Dies sollte jedoch
                 nur in besonderen Fällen erfolgen, da das Uni-Logo nach
                 CD Richtlinien i.d.R. in der oberen rechten Ecke
                 platziert werden sollte.

                 Wird das optionale Argument verwendet, jedoch kein Pfad
                 angegeben, so wird auch kein Logo in der rechten oberen
                 Ecke angezeigt.

                 Wird das optionale Argument weggelassen, so wird
                 standardmäßig das Uni-Logo in der rechten oberen
                 Ecke präsentiert.

> \unititlepage[graphic=graphics/indoor_sw, partnerlogo=graphics/PHTG_logo]%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 10. Thesis-Titelseite        %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Mit Hilfe des Makros

    \thesistitlepage

kann die Titleseite des Dokumentes an die Vorgaben
einer Arbeit (Bachelorarbeit, Masterarbeit, ... ) des
Fachbereichs Informatik und Informationswissenschaft
angepasst werden.

Das Makro besitzt ein festes und ein optionales Argument.

    \unititlepage[language=<language>]{<Art der Arbeit>}

Dabei stehen folgende Optionen zur Verfügung:

    language        Mit diesem Optionalen Argument kann die
                    Sprache der Titelseite angepasst werden.

                    Mögliche Werte sind

                        german
                        english

                    Je nach dem übergebenen Wert, wird die Titelseite
                    entweder auf Deutsch oder English erstellt.

                    Sollte diese Option weggelassen werden, wird
                    die Titelseite auf Deutsch erstellt.

    Art der Arbeit  Hier kann die Art der Arbeit übergeben werden,
                    welche auf der Titelseite erscheint.

                    Hier kann alles übergeben werden. Normalerweise
                    wird hier Bachelorarbeit, Masterarbeit, o.ä.
                    angegeben.

Diese Thesis-Titelseite ist auf DinA4 Hochformat optimiert!

> \thesistitlepage[language=german]{Bachelorarbeit}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 11. Inhalts-, Tabellen- und Abbildungsverzeichnis %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Das Inhaltsverzeichnis kann wie gewohnt mit dem Makro

    \tableofcontents

erstellt werden.

> \tableofcontents


Das Abbildungsverzeichnis kann wie gewohnt mit dem Makro

    \listoffigures

erstellt werden.

Möchte man das Abbildungsverzeichnis zum Inhaltsverzeichnis
hinzufügen, so kann dies mit dem Makro

    \addcontentsline{toc}{chapter}{Abbildungsverzeichnis}

hinzugefügt werden.

> \listoffigures
> \addcontentsline{toc}{chapter}{Abbildungsverzeichnis}


Das Tabellenverzeichnis kann wie gewohnt mit dem Makro

    \listoftables

erstellt werden.

Möchte man das Tabellenverzeichnis zum Inhaltsverzeichnis
hinzufügen, so kann dies mit dem Makro

    \addcontentsline{toc}{chapter}{Tabellenverzeichnis}

hinzugefügt werden.

> \listoftables
> \addcontentsline{toc}{chapter}{Tabellenverzeichnis}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 12. Kapitel, Abschnitte, ... %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Kapitel, Abschnitte, Unterabschitte und Unterunterabschnitte
können wie gewohnt mit den Makros

    \chapter{...}
    \section{...}
    \subsection{...}
    \subsubsection{...}

erstellt werden.

Diese werden dann nach den Corporate Design Richtlinien der
Univeristät Konstanz erstellt.

Sollte das Style Add-on geladen werden, werden alternative
Überschriften erstellt, die nicht mehr den CD-Richtlinen
der Universität Konstanz entsprechen, jedoch für Abschluss-
arbeiten verwendet werden können.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 13. Aufzählung               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Aufzählungen, sowohl numerisch mittels

    enumerate

als auch nicht-numerisch mittels

    itemize

können nach den Designvorlagen der Universität Konstanz
erstellt werden. Außerdem sind auch verschiedene Ebenen möglich.

> \begin{enumerate}
> \item Studienbereitschaft (Nummerische Aufzählung)
> \begin{itemize}
> \item Profil der Befragten (Absatzformat Aufzählungszeichen)
> \item Anteil der Studierenden mit Migrationshintergrund
> \item Anteil der Studierenden
> \end{itemize}
> \item Vor dem Studium und Studieneinstieg
> \begin{itemize}
> \item Studienentscheidung bzw. Studienwahl (Absatzformat Aufzählungszeichen)
> \item Angebnote zur Studieneinstiegsphase
> \item Schwierigkeiten in der Studieneinstiegsphase
> \end{itemize}
> \end{enumerate}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 14. Abbildung                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Auch Abbildungen können wie gewohnt mit der figure Umgebung
im Corporate Design der Universität Konstanz erstellt werden.

> \begin{figure}[H]
> \includegraphics[width=\textwidth]{graphics/indoor_sw.png}
> \caption{Verteilung der Studenten auf der Treppe}
> \label{fig:treppe}
> \end{figure}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 15. Tabelle                  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Um eine Tabelle im Corporate Design der Universität Konstanz
zu erstellen wird das Paket tabu verwendet. Dadurch ergeben
sich auch kleine Unterschiede beim Erstellen von Tabellen.

Als Umgebung muss tabu anstatt tabular verwendet werden:

    \begin{tabu}

        ...

    \end{tabu}

Die Spalten können direkt im Anschluss definiert werden.

    { X[coef, align, type] X[coef, align, type] ... }

    - coef skaliert die Spalten, sollten es mehrere sein
    - align ist entweder r, l, c oder j
    - type ist entweder p (Standard), m oder b
    - Vertikale Linien können mittels | zwischen den Spalten
      gezeichnet werden. Dies sollte aus ästehtischen Gründen
      jedoch wenn möglich vermieden werden.

Danach können wie aus der tabular Umgebung gewohnt die
Zeilen definiert werden. Die Spalte wird mit % gewechselt und
ein Zeilenumbruch kann mit \\ eingeleitet werden.

Möchte man eine horizontale Linie zeichnen, so können nach
dem Corporate Design der Universität Konstanz entweder

    \unitoprule

für eine durchgezogene (dicke) Linie in seeblau oder

    \unimidrule

eine gestrichelte durchgezogene Linie in seeblau gezeichnet
werden.

Da die tabu Umgebung sehr mächtig ist, können auch weitere
Varianten gezeichnet werden. Dazu sein an die Paketdokumentation
verwiesen:

    ftp://ftp.fu-berlin.de/tex/CTAN/macros/latex/contrib/tabu/tabu.pdf

Ein ausführliches Beispiel folgt gleich weiter unten.

Die Tabelle sollte in einer table Umgebung eingebunden werden, damit
sie im Tabellenverzeichnis erscheint. Außerdem kann noch eine Tabellen-
überschrift hinzugefügt werden.

> \begin{table}
> \caption{Universitätsstatistik}
> \label{tbl:Uni}
> \selectfontsize{10pt}
> \begin{tabu} {X[l]X[r]X[r]X[r]X[r]X[r]}
> \unitoprule \\
> \textbf{Wintersemester} & \textbf{2009/10} & \textbf{2010/11} & \textbf{2011/12} & \textbf{2012/13} & \textbf{2013/14} \\
> \unitoprule \\
> Mathematik & 456 & 428 & 526 & 542 & 529 \\
> \unimidrule \\
> Informatik & 266 & 308 & \ldots \\
> \unimidrule \\
> \ldots \\
> \unimidrule \\
> \\
> \unimidrule \\
> \\
> \unitoprule \\
> \textbf{Gesamt} & \textbf{9528} & \textbf{10081} & \textbf{10645} & \textbf{11337} & \textbf{11772} \\
> \unitoprule \\
> \end{tabu}
> \end{table}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 16. Farben des Corporate Design %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Es stehen natürlich auch die Farben des Corporate Designs zur Verfügung:

  Schlüssel   Beschreibung
  --------------------------------------------------------------
  seeblau100  Seeblau mit der Sättigungsstufe 100%
  seeblau65   Seeblau mit der Sättigungsstufe 65%
  seeblau35   Seeblau mit der Sättigungsstufe 35%
  seeblau20   Seeblau mit der Sättigungsstufe 20%

  schwarz60   Seeblau - SW-Umsetzung mit der Sättigungsstufe 60%
  schwarz40   Seeblau - SW-Umsetzung mit der Sättigungsstufe 40%
  schwarz20   Seeblau - SW-Umsetzung mit der Sättigungsstufe 20%
  schwarz10   Seeblau - SW-Umsetzung mit der Sättigungsstufe 10%

Möchte man beispielsweise einen Text mit Seeblau in der Sättigungsstufe
100% schreiben, so kann das bereits existierende Makro

> \textcolor{<Schlüssel der Farbe>}{<Zu färbenden Text>}

verwendet werden.


Somit erstellt folgender Befehl zunächst ein Textfeld an der Koordinate (3 cm,
\paperheight - 3cm) mit einer maximalen Breite, da es eh aus nur einer Zeile besteht
und dem blauen, fetten und kursiv geschriebenen Text:

    -- uni-konstanz.de


> \begin{textfeld}{3cm}{\paperheight - 3cm}%
> \textcolor{seeblau100}{\textbf{\textit{-- uni-konstanz.de}}}
> \end{textfeld}%



%%%%%%%%%%%%%%%%%%%%%%
% 17. Schriftgröße   %
%%%%%%%%%%%%%%%%%%%%%%

Da innerhalb einer Arbeit es meistens mehrere verschiedene Schriftgrößen
gibt, steht hier das Makro

     \selectfontsize

zur Verfügung.

Es kann jedoch auch die Latex internen Makros wie \Large, \small, o.ä.
verwendet werden.

Dieses Makro besitzt ein unbedingt notwendiges Argument und ein optionales
Feld, indem Key-Value Pairs übergeben werden können.

     \selectfontsize[<Key Value Pairs>]{<Schriftgröße>}

Das Argument hat dabei folgende Bedeutung:

   1. Argument:         Hier wird die neue Schriftgröße angegeben, die verwendet werden
                        soll.
Die weiteren Formatierungsoptionen werden alle innerhalb des optionalen Argumentes mittels
Key-Value Pairs bestimmt.

Dabei stehen folgende Optionen zur Verfügung:

     baselineskip    Hier wird der baselineskip angegeben, welcher verwendet werden soll
                     Mögliche Werte:
                         0      Ist dieser 0, dann wird der baselinefaktor verwendet
                         sonst
                    Standardwert: 0

     baselinefaktor Hier wird der Faktor angegeben, der verwendet wird, um den neuen
                    baselineskip zu berechnen.
                    Dieser wird nur benutzt, falls der baselineskip 0 beträgt.

                        baselineskip = baselinefaktor * #1

                    Standardwert: 12/10

                    Da hier keine Fließkommazahl in der Dezimalschreibweise angegeben werden
                    kann, müssen diese als Brüche repräsentiert werden, wie z.b. 12/10 anstatt
                    1.2.

Zurück zur Standardgröße gelangt man mit \normalsize

> \selectfontsize[baselinefaktor=14/10]{70pt}
> \normalsize



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 18. CD Element: Markieren    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Um einen Text mit Hilfe des Markieren Elements des Corporate Design hervorzuheben,
steht das Makro

    \markieren

zur Verfügung.

Dieses Makro besitzt vier unbedingt notwendige Argumente und ein optionales
Feld, indem weitere EIgenschaften festgelegt werden könnnen..

    \markieren[Optionen per Key-Value Pair]{<Zeile 1>}{<Zeile 2>}{<Zeile 3>}{<Zeile 4>}

Die Argumente haben dabei folgende Bedeutung:

  1. - 4. Argument:    Hier werden nun die eigentlichen Zeilen übergeben.

                       Wichtig dabei ist es, dass die Aufteilung der Zeilen manuell erfolgen muss durch
                       die Argumente, da nur somit sichergestellt werden kann, dass bspw. Treppeneffekte
                       nicht auftreten und somit der Benutzer alle Freiheiten bei der Aufteilung besitzt.

                       Sollten nicht alle Zeilen verwendet werden, dann müssen die hinteren Brackets
                       leer gelassen werden, wie beispielsweise bei der Headline

Die wichtigen Formatierungsoptionen werden alle innerhalb des optionalen Argumentes mittels
Key-Value Pairs bestimmt.

Dabei stehen folgende Optionen zur Verfügung:

  align                Hier kann angegeben werden, ob das komplette Objekt
                       links- oder rechtsbündig angeordent werden soll.

                       Der Standardwert ist "left" und somit linksbündig.

                       Für eine rechtsbündige Anordnung muss hier der Wert "right" hinterlegt werden.

  vertical             Hier wird angegeben, ob der Inhalt der Zeilen zentriert werden soll oder
                       überall an der gleichen Baseline ausgerichtet werden soll.

                       Dies kann mittels der Wörter "center" und "base" eingestellt werden.
                       Dabei ist "center" als Standardwert festgelegt.

                       Der Unterschied besteht darin, dass bei Zeilen die Buchstaben mit einer Tiefe
                       enthalten, wie g, p oder q, anders zentriert werden als welche ohne Buchstaben
                       mit einer Tiefe.

                       Da dies ein wenig Geschmackssache ist, werden hier beide Varianten zur Verfügung
                       gestellt, wobei "center" primär verwendet werden soll, und "base" eher wenn
                       Buchstaben mit einer Tiefe in den Zeilen enthalten sind.


Somit erstellt folgender Befehl zunächst ein Textfeld an der Koordinate (1 cm, 12 cm)
mit einer maximalen Breite, da zunächst nicht sicher ist, wie breit dieses Textfeld
wird und als Inhalt eines neuen Markieren Elements, welches aus den drei Zeilen

    Wir sind
    nah am Wasser
    gebaut

besteht. Zudem sind alle Zeilen an der Baseline ausgerichtet.

> \begin{textfeld}{1cm}{12cm}%
> \markieren[vertical=base]{\textbf{Wir sind}}{\textbf{nah am Wasser}}{\textbf{gebaut}}{}%
> \end{textfeld}%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 19. CD Element: Unterstreichen %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Um einen Text mit Hilfe des Unterstreichen Elements des Corporate Design hervorzuheben,
steht das bereits bekannte Makro

    \underline

zur Verfügung, welches an die Anforderungen des Corporate Designs angepasst wurde.

Dieses Makro besitzt ein notwendiges Argument

    \underline{1. Argument}

Das Argument hat folgende Bedeutung:

  1. Argument: Hier wird der zu unterstreichende Text hinterlegt.

Wichtig ist noch zu wissen, dass auch Textbrüche ohne Probleme durchgeführt werden
können.

Zudem können weitere Formatierungen, wie bold oder italic innerhalb des Argumentes
angewendet werden.

Die Dicke der unterstrichenen Linie passt sich dabei der aktuell verwendeten
Textgröße an.


Somit erstellt folgender Befehl zunächst ein Textfeld an der Koordinate (3 cm,
\paperheight - 6cm) mit einer maximalen Breite, da hier die Zeilenumbrüche selbst
angegeben werden. Innerhalb des Textfeldes befindet sich ein Fließtext, welcher
die Wörter

    einzigartigen Umgebung direkt am Bodensee

unterstreicht und sie mittels \textbf{...} noch fett hervorhebt.

> \begin{textfeld}{3cm}{\paperheight - 6cm}%
> Außer einer \underline{\textbf{einzigartigen Umgebung direkt am Bodensee}} haben\\
> wir noch einiges zu bieten. Interessiert? Dann besuchen Sie uns unter:
> \end{textfeld}%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 20. CD Element: Merken       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Um einen Text mit Hilfe des Merken Elements des Corporate Design hervorzuheben,
steht das Makro

    \merken

zur Verfügung.

Dieses Makro besitzt drei unbedingt notwendige Argumente

    \merken{1. Argument}{2. Argument}{3. Argument}

Die Argumente haben dabei folgende Bedeutung:

  1. Argument: Hier wird die Breite des kompletten Objektes angegeben. Da das
               Merken Objekt quadratisch ist, wird hier sowohl die Breite als auch
               die Höhe angegeben.

  2. Argument: Hier wird die Subline des Merken Elementes angegeben, die direkt unter
               der Zeile mit dem X folgt (siehe auch Corporate Design Manual).

  3. Argument: Hier wird der eigentliche Inhalt angegeben. Wichtig hierbei ist es,
               dass dieser Inhalt an die untere Kante des Merken Elementes orientiert
               ist. Somit entgegen der Subline (2. Argument), welche an die obere
               Kante abzüglich der Zeile mit dem X orientiert ist.

Hier folgt noch eine grafische Darstellung der Argumente:

   |<------- 1. Argument ------->|

   -------------------------------    -
   |                           X |    ^
   | Subline (2. Argument)       |    |
   |                             |    1
   |                             |    .
   |                             |    A
   |                             |    r
   |                             |    g
   |                             |    u
   |                             |    m
   |                             |    e
   |                             |    n
   |                             |    t
   |                             |    |
   | Inhalt (3. Argument)        |    v
   -------------------------------    -

Wichtig ist noch zu wissen, dass die Linienstärke und die Größe des X in der rechten
oberen Ecke an die Höhe / Breite des Merken Elements dynamisch angepasst ist.


Somit erstellt folgender Befehl zunächst ein Textfeld an der Koordinate
(\paperwidth - 7.5cm, \paperheight - 7.5cm) mit einer maximalen Breite, da es nur
aus dem Merken Element besteht und dies eine feste Breite besitzt.

Der Inhalt ist wie bereits angesprochen ein Merken-Element mit einer Breite und Höhe
von 6.5 cm, einer leeren Subline und einem textuellen Inhalt:

   Die Universität Konstanz ist seit 2007 in allen drei Förderlinien der
   Exzellenzinitiative erfolgreich.

Die Koordinaten des Textfeldes wurden hier so ausgewählt, damit das Textfeld in der
rechten unteren Ecke platziert wird mit jeweils einem Abstand von 1 cm zum Rand
(6.5 cm + 1 cm = 7.5 cm).

> \begin{textfeld}{\paperwidth - 7.5cm}{\paperheight - 7.5cm}%
> \merken{6.5cm}{}{Die Universität Konstanz ist seit 2007 in allen drei Förderlinien
  der Exzellenzinitiative erfolgreich.}
> \end{textfeld}%



%%%%%%%%%%%%%%%%%%%%%%%%%%
% 21. CD Element: Block  %
%%%%%%%%%%%%%%%%%%%%%%%%%%

Mit dem Makro

    \cdblock[Optionen per Key-Value Pair]{<Headline>}{<Spalte 1>}{<Spalte 2>}{<Spalte 3>}{<Spalte 4>}{<Spalte 5>}{<Spalte 6>}{<Spalte 7>}{<Spalte 8>}

können Block-Elemente für z.B. wisschenschaftliche Inhalte erstellt werden.

Dieses Makro besitzt 9 erforderliche Elemente, die bei jedem Aufruf angegeben werden müssen. Dabei
ist es natürlich mögliche Argumente leer zu lassen, falls man diese nicht benötigt. Dies hat jedoch
keinen Einfluss auf die Anzahl an Spalten. Diese müssen separat im Optionenargument angegeben werden
mittels des Schlüssels columnnum (siehe weiter unten).

Die Argumente haben dabei folgende Bedeutung:

  1. Argument: Inhalt der Headline
  2. Argument: Inhalt der 1. Spalte
  3. Argument: Inhalt der 2. Spalte
  4. Argument: Inhalt der 3. Spalte
  5. Argument: Inhalt der 4. Spalte
  6. Argument: Inhalt der 5. Spalte
  7. Argument: Inhalt der 6. Spalte
  8. Argument: Inhalt der 7. Spalte
  9. Argument: Inhalt der 8. Spalte


Die wichtigen Formatierungsoptionen werden diesmal alle innerhalb des optionalen Argumentes mittels
Key-Value Pairs bestimmt.

Dabei stehen folgende Optionen zur Verfügung:

    thick          Hier wird die Dicke der Linie bestimmt.
                   Die Pfeile werden generell mit der doppelten Dicke gezeichnet!
                   Standardwert: \boxlinewidth

    color          Hier wird die Farbe der Linie angegeben
                   Es sollten nur die folgenden Farben benutzt werden:
                       seeblau100
                       seeblau65
                       seeblau35
                       seeblau20
                       black
                       schwarz60
                       schwarz40
                       schwarz20
                       schwarz10
                   Standardwert: seeblau100

    width          Hier wird die Breite des Blocks angegeben
                   Standardwert: \paperwidth

    columnnum      Hier werden die Anzahl an Spalten definiert
                   Standardwert: 4

    headlinesep    Hier wird der Abstand zwischen der Headline und den Spalten angegeben
                   Standardwert: Aktuelle Schriftgröße

    columnspace    Hier wird der Abstand zwischen den Spalten angegeben
                   Standardwert: Doppelte Schriftgröße

    block          Hier kann angegeben werden, ob man einen Rahmen um diesen Block haben möchte
                   Mögliche Werte: true, false
                   Standardwert: false

    inner          Hier kann angegeben werden, ob zwischen den Spalten Trennlinien haben möchte
                   Mögliche Werte:
                       false    keine Trennlinien
                       short    Trennlinien, die so lange sind, wie der längste Nachbar (entweder der
                                linke oder rechte Nachbar
                       long     Trennlinien, die bis nach ganz unten gehen. Sie sind also so lang
                                wie die längste Spalte
                   Standardwert: false

    inner1,        Hier kann für jeden Zwischenraum der Spalte exakt angegeben werden, ob Trennlinien
    inner2,        existieren sollen und falls ja, wie lang sie sein sollen. Diese Werte werden jedoch
    inner3,        nur berücksichtigt, wenn inner=false ist. Ansonsten ist inner stärker.
    inner4,        Mögliche Werte:
    inner5,           false    keine Trennlinien
    inner6,           short    Trennlinien, die so lange sind, wie der längste Nachbar (entweder der
    inner7                     linke oder rechte Nachbar
                      long     Trennlinien, die bis nach ganz unten gehen. Sie sind also so lang
                               wie die längste Spalte
                   Standardwert: false

    outerleft,     Hier kann angegeben werden, ob links (rechts) der ersten Spalte eine Trennlinie existieren soll.
    outerright     Mögliche Werte
                       false    keine Trennlinien
                       short    Trennlinien, die so lange sind, wie der direkte Nachbar (bei outerleft die 1. Spalte
                                und bei outerright die letzte Spalte
                       long     Trennlinien, die bis nach ganz unten gehen. Sie sind also so lang
                                wie die längste Spalte
                       verylong Trennlinie geht von oben nach unten, sowie ein halber columnspace nach innen.
                   Standardwert: false

    outertop,      Hier kann angegeben werden, ob oberhalb (unterhalb) des Blocks eine Trennlinie, oder ein Pfeil existieren soll.
    outerbottom    Mögliche Werte
                       false    keine Trennlinien
                       long     Trennlinien, die von links nach rechts geht
                       verylong Trennlinie, die von links nach rechts geht, sowie ein halber columnspace nach oben (unten).
                       arrow    Pfeil, der aus der Trenlinie verylong besteht und in der Mitte einen Pfeil nach oben (unten)
                                besitzt.
                   Standardwert: false

    arrowtop1left, Hier kann angegeben werden, ob zwei Spalten oberhalb des Blocks mittels eines Doppelpfeils verbunden werden
    arrowtop1right sollen. Da es maximal 8 Spalten sind, können auch nur maximal 4 Paare bestimmt werden.
    arrowtop2left  Ein Paar besteht somit aus einer linken und einer rechten Spalte.
    arrowtop2right Mögliche Werte:
    arrowtop3left      0   Keine Auswahl
    arrowtop3right     1-8 Auswahl einer Spalte von 1 bis 8
    arrowtop4left  Standardwert: 0
    arrowtop4right Sollte der linke Wert nicht kleiner als der rechte Wert sein, so werden keine Pfeile gezeichnet. Das gleiche
                   gilt für Werte, die außerhalb des Bereichs liegen.


Wichtig ist noch zu wissen, wie die Breite letztendlich berechnet wird:
Da es auch links und rechts der Spalten Trennlinien oder Pfeile geben kann, ist links der 1. und rechts der
letzten Spalte ebenfalls ein columnspace vorgesehen.
Somit wird die Spaltenbreite wie folgt berechnet

    blockcolumnwidth = (width - (columnspace * (columnnum + 1))) / columnnum


Beispiele finden Sie in den .tex Dateien.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 22. CD Element: Linie (mit optionalen Pfeilen) %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Mit dem Makro

    \cdline[Optionen per Key-Value Pair]{<Länge der Linie>}

kann eine Linie mit einer bestimmten Länge erstellt werden.

Dieses Makro besitzt 1 erforderliches Element, welches bei jedem Aufruf mit angegeben
werden muss.

Das Argument hat dabei folgende Bedeutung.

  1. Argument: Länge der erzeugten Linie


Die wichtigen Formatierungsoptionen werden alle innerhalb des optionalen Argumentes mittels
Key-Value Pairs bestimmt.

Dabei stehen folgende Optionen zur Verfügung:

    thick          Hier wird die Dicke der Linie bestimmt
                   Standardwert: \boxlinewidth

    mode           Hier wird angegeben, ob die Linie horizontal oder vertikal ausgerichtet werden soll
                   Mögliche Werte
                       horizontal
                       vertical
                   Standardwert: horizontal

    color          Hier wird die Farbe der Linie angegeben
                   Es sollten nur die folgenden Farben benutzt werden:
                       seeblau100
                       seeblau65
                       seeblau35
                       seeblau20
                       black
                       schwarz60
                       schwarz40
                       schwarz20
                       schwarz10
                   Standardwert: seeblau100

    arrowleft      Hier wird angegeben, die Linie am linken (vertical: oberen) Ende mit einem Pfeil enden soll
                   Mögliche Werte:
                       true
                       false
                   Standardwert: false

    arrowright     Hier wird angegeben, die Linie am rechten (vertical: unteren) Ende mit einem Pfeil enden soll
                   Mögliche Werte:
                       true
                       false
                   Standardwert: false


Erstellt eine Linie mit der Standardfarbe seeblau100, einer Länge von 10cm,
einer Dicke von 8pt und einem linken und rechten Pfeil.

> \cdline[thick=8pt, arrowleft=true, arrowright=true]{10cm}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 23. CD Element: Klammer (mit optionalen Pfeilen) %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Mit dem Makro

    \cdbracket[Optionen per Key-Value Pair]{<Breite des Klammer>}{<Höhe des Klammer>}

kann eine Klammer mit einer bestimmten Breite und Höhe gezeichnet werden.

Dieses Makro besitzt 2 erforderliche Elemente, welche bei jedem Aufruf mit angegeben
werden müssen.

Die Argumente haben dabei folgende Bedeutung.

  1. Argument: Breite der erzeugten Klammer
  2. Argument: Höhe der erzeugten Klammer


Die wichtigen Formatierungsoptionen werden alle innerhalb des optionalen Argumentes mittels
Key-Value Pairs bestimmt.

Dabei stehen folgende Optionen zur Verfügung:

    thick          Hier wird die Dicke der Linien bestimmt
                   Standardwert: \boxlinewidth

    mode           Hier wird die Ausrichtung der Klammer angegeben
                   Mögliche Werte
                       left    linke Klammer
                       top     obere Klammer
                       right   rechte Klammer
                       bottom  untere Klammer
                   Standardwert: left

    color          Hier wird die Farbe der Linie angegeben
                   Es sollten nur die folgenden Farben benutzt werden:
                       seeblau100
                       seeblau65
                       seeblau35
                       seeblau20
                       black
                       schwarz60
                       schwarz40
                       schwarz20
                       schwarz10
                    Standardwert: seeblau100

    arrowleft      Hier wird angegeben, ob die Klammer am linken (oberen) Ende mit einem Pfeil enden soll
                   Mögliche Werte:
                       true
                       false
                   Standardwert: false

    arrowright     Hier wird angegeben, ob die Klammer am rechten (unteren) Ende mit einem Pfeil enden soll
                   Mögliche Werte:
                       true
                       false
                   Standardwert: false

    arrowmiddle    Hier wird angegeben, ob die Klammer in der Mitte einen weiteren Pfeil besitzen soll der in die
                   andere Richtung der Klammer zeigt (wie beim Makro \block mit der Optione arrow bei outerbottom / outertop)
                   Mögliche Werte:
                       true
                       false
                   Standardwert: false


Erstellt eine rechte Klammer, die einen Pfeil in der Mitte nach links besitzt.
Die Breite beträgt 5 cm und die Höhe 23.6 cm.

> \cdbracket[mode=right, arrowmiddle=true]{5cm}{23.6cm}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 24. Literaturverzeichnis     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Zum Schluss kann noch das Literaturvzerzeichnis hinzugefügt
% werden.
%
% Damit es ebenfalls im Inhaltsverzeichnis gefunden werden kann,
% sollte das Literaturverzeichnis mit dem Makro
%
%    \addcontentsline{toc}{chapter}{Literaturverzeichnis}
%
% hinzugefügt werden.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 25. Sonstiges                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Bei Fragen, Hinweisen und Anregungen können Sie mich unter

   michael.brendle@uni-konstanz.de

kontaktieren.
