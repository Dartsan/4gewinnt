[Bild_HouseBuilder]:https://refactoring.guru/images/patterns/diagrams/builder/solution1.png?id=8ce82137f8935998de802cae59e00e11
# Design Pattern Herunter
## Builder Design Pattern
### Idee
Das Builder Pattern ermöglicht es mehrere, verschiedene Objekte aus einem "Bauplan" zu erstellen. So wird die Erstellung von sehr komplexen Objekten in kleinere Probleme unterteilt und somit realisiert.

### Problem
Bei sehr komplexen Objekten ist oft auch der "Bauplan" sehr komplex und es besteht aus sehr vielen verschachtelten Objekten. Dadurch wird der Code sehr unstruktiert, unübersichtlich, unlesbar und schwer wartbar. Bei sehr vielen möglichen Parametern, die aber nicht alle bei jedem Objekt vorkommen, kommt es schnell zu einer sehr hohen Anzahl an verschachtelten Objekten mit den verschiedenen Kombinationen der Parameter.
Eine andere Möglichkeit wäre es einen riesigen "Bauplan" mit allen Parametern die für alle möglichen Objekte benötigt werden, zu machen. Darin birgt sich aber das Problem, dass viele der Parameter sehr selten gebraucht werden und "Bauplan" selbst dann rieisig und unübersichtlich wird.

### Lösung
Der Bauplan für ein bestimmtes Produkt des Objekts wird von der eigenen Klasse herausgenommen und und in sogenannte **Builder** verschoben. Mit dieser Verschiebung der einzelnen Schritte in **Builder** wird ein schrittweises Erschaffen der Objekte ermöglicht. Da es verschiedene **Builder** für den gleichen Parameter geben kann, werden verschiedene Repräsentationen des gleiche Objekts ermöglicht.
Um das Aufrufen der Builder zu erleichtern, gibt es sogenannte **Directors**. Diese enthalten eine fix vorgegebene Reihenfolge an auszführenden Builders, sind aber nicht zwingend notwendig.

### Beispeil
Um das Builder Pattern verständlicher darzustellen, schauen wir es uns anhand des Beispiels eines Haus an:

![Beispiel Haus][Bild_HouseBuilder]

- Die verschiedenen Produkte des Hauses werden mithilfe der **Builder** erschaffen. (z.B. Wand, Dach, Tür, Fenster, Garage, etc.)
- Ein Builder kann verschiedene Arten des Produktes erschaffen (z.B. Wände aus verschiedenem Material, Türen in verschiedenen Farben)
- Ein **Director** kann eine Reihenfolge der Builder enthalten (z.B. zuerste die Wände aufstellen, danach das Dach darauf setzen und die Fenster einbauen)

### Vorteile
- Die Objekte werden schrittweise erstellt.
- Verschiedene Repräsentationen von Objekten können mit demselben Bauplan erschafft werden.
- Der komplexe Code kann aufgeteilt werden und das große Problem wird somit in mehrere kleinere Probleme zerteilt.
### Nachteil
- Allgemein wird die Komplexität des Codes nicht wirklich verringert sondern erhöht, da viele neue Klassen (Builders und Directors) erstellt werden

Quelle: <https://refactoring.guru/design-patterns/builder>
