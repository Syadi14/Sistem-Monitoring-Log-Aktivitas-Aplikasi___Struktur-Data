error id: 4AA441D22BC0218C5DE6A85E68736031
file:///C:/Users/hafid/Documents/Kuliah/Coding/Semester-4/Pemrog/latihan-uas-1.scala
### java.lang.AssertionError: assertion failed

occurred in the presentation compiler.



action parameters:
uri: file:///C:/Users/hafid/Documents/Kuliah/Coding/Semester-4/Pemrog/latihan-uas-1.scala
text:
```scala
// id produk
// jumlah barang
// harga satuan

// transaksi besar = minJumlah

import scala.io.StdIn.readline

class Transaksi(idProduk" int, jumlahBarang: int, hargaSatuan: int)
```


presentation compiler configuration:
Scala version: 3.8.3-bin-nonbootstrapped
Classpath:
<WORKSPACE>\.scala-build\Coding_d5c0a6989e\classes\main [exists ], <HOME>\AppData\Local\Coursier\cache\v1\https\repo1.maven.org\maven2\org\scala-lang\scala3-library_3\3.8.3\scala3-library_3-3.8.3.jar [exists ], <HOME>\AppData\Local\Coursier\cache\v1\https\repo1.maven.org\maven2\org\scala-lang\scala-library\3.8.3\scala-library-3.8.3.jar [exists ], <HOME>\AppData\Local\Coursier\cache\v1\https\repo1.maven.org\maven2\com\sourcegraph\semanticdb-javac\0.10.0\semanticdb-javac-0.10.0.jar [exists ], <WORKSPACE>\.scala-build\Coding_d5c0a6989e\classes\main\META-INF\best-effort [missing ]
Options:
-Xsemanticdb -sourceroot <WORKSPACE> -Ywith-best-effort-tasty




#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:13)
	dotty.tools.dotc.parsing.Scanners$Scanner.lookahead(Scanners.scala:1130)
	dotty.tools.dotc.parsing.Parsers$Parser.termParamClause$$anonfun$1(Parsers.scala:3825)
	dotty.tools.dotc.parsing.Parsers$Parser.enclosedWithCommas(Parsers.scala:628)
	dotty.tools.dotc.parsing.Parsers$Parser.inParensWithCommas(Parsers.scala:641)
	dotty.tools.dotc.parsing.Parsers$Parser.termParamClause(Parsers.scala:3847)
	dotty.tools.dotc.parsing.Parsers$Parser.recur$7(Parsers.scala:3861)
	dotty.tools.dotc.parsing.Parsers$Parser.termParamClauses(Parsers.scala:3869)
	dotty.tools.dotc.parsing.Parsers$Parser.classConstr(Parsers.scala:4338)
	dotty.tools.dotc.parsing.Parsers$Parser.classDefRest(Parsers.scala:4329)
	dotty.tools.dotc.parsing.Parsers$Parser.classDef(Parsers.scala:4325)
	dotty.tools.dotc.parsing.Parsers$Parser.tmplDef(Parsers.scala:4301)
	dotty.tools.dotc.parsing.Parsers$Parser.defOrDcl(Parsers.scala:4065)
	dotty.tools.dotc.parsing.Parsers$Parser.topStatSeq(Parsers.scala:4840)
	dotty.tools.dotc.parsing.Parsers$Parser.topstats$1(Parsers.scala:5036)
	dotty.tools.dotc.parsing.Parsers$Parser.compilationUnit$$anonfun$1(Parsers.scala:5041)
	dotty.tools.dotc.parsing.Parsers$Parser.checkNoEscapingPlaceholders(Parsers.scala:555)
	dotty.tools.dotc.parsing.Parsers$Parser.compilationUnit(Parsers.scala:5046)
	dotty.tools.dotc.parsing.Parsers$Parser.parse(Parsers.scala:207)
	dotty.tools.dotc.parsing.Parser.parse$$anonfun$1(ParserPhase.scala:32)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	dotty.tools.dotc.core.Phases$Phase.monitor(Phases.scala:533)
	dotty.tools.dotc.parsing.Parser.parse(ParserPhase.scala:40)
	dotty.tools.dotc.parsing.Parser.$anonfun$2(ParserPhase.scala:52)
	scala.collection.Iterator$$anon$6.hasNext(Iterator.scala:495)
	scala.collection.Iterator$$anon$9.hasNext(Iterator.scala:597)
	scala.collection.immutable.List.prependedAll(List.scala:156)
	scala.collection.immutable.List$.from(List.scala:681)
	scala.collection.immutable.List$.from(List.scala:681)
	scala.collection.IterableOps$WithFilter.map(Iterable.scala:906)
	dotty.tools.dotc.parsing.Parser.runOn(ParserPhase.scala:51)
	dotty.tools.dotc.Run.runPhases$1$$anonfun$1(Run.scala:380)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.ArrayOps$.foreach$extension(ArrayOps.scala:1324)
	dotty.tools.dotc.Run.runPhases$1(Run.scala:373)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1$$anonfun$2(Run.scala:420)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1$$anonfun$adapted$1(Run.scala:420)
	scala.Function0.apply$mcV$sp(Function0.scala:42)
	dotty.tools.dotc.Run.showProgress(Run.scala:482)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1(Run.scala:420)
	dotty.tools.dotc.Run.compileUnits$$anonfun$adapted$1(Run.scala:432)
	dotty.tools.dotc.util.Stats$.maybeMonitored(Stats.scala:69)
	dotty.tools.dotc.Run.compileUnits(Run.scala:432)
	dotty.tools.dotc.Run.compileSources(Run.scala:319)
	dotty.tools.dotc.interactive.InteractiveDriver.run(InteractiveDriver.scala:165)
	dotty.tools.pc.CachingDriver.run(CachingDriver.scala:44)
	dotty.tools.pc.WithCompilationUnit.<init>(WithCompilationUnit.scala:29)
	dotty.tools.pc.SimpleCollector.<init>(PcCollector.scala:362)
	dotty.tools.pc.PcSemanticTokensProvider$Collector$.<init>(PcSemanticTokensProvider.scala:60)
	dotty.tools.pc.PcSemanticTokensProvider.Collector$lzyINIT1(PcSemanticTokensProvider.scala:60)
	dotty.tools.pc.PcSemanticTokensProvider.Collector(PcSemanticTokensProvider.scala:60)
	dotty.tools.pc.PcSemanticTokensProvider.provide(PcSemanticTokensProvider.scala:83)
	dotty.tools.pc.ScalaPresentationCompiler.semanticTokens$$anonfun$1(ScalaPresentationCompiler.scala:155)
	scala.meta.internal.pc.CompilerAccess.withSharedCompiler(CompilerAccess.scala:149)
	scala.meta.internal.pc.CompilerAccess.$anonfun$1(CompilerAccess.scala:93)
	scala.meta.internal.pc.CompilerAccess.onCompilerJobQueue$$anonfun$1(CompilerAccess.scala:210)
	scala.meta.internal.pc.CompilerJobQueue$Job.run(CompilerJobQueue.scala:153)
	java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1090)
	java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:614)
	java.base/java.lang.Thread.run(Thread.java:1474)
```
#### Short summary: 

java.lang.AssertionError: assertion failed