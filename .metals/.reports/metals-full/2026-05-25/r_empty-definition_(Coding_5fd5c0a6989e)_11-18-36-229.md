error id: file:///C:/Users/hafid/Documents/Kuliah/Coding/Semester%204/scala3/StatistikKalimat.scala:map
file:///C:/Users/hafid/Documents/Kuliah/Coding/Semester%204/scala3/StatistikKalimat.scala
empty definition using pc, found symbol in pc: 
semanticdb not found

found definition using fallback; symbol map
offset: 188
uri: file:///C:/Users/hafid/Documents/Kuliah/Coding/Semester%204/scala3/StatistikKalimat.scala
text:
```scala
import scala.io.StdIn

class SentenceStats(val sentence: String) {

  private val vowels = Set('a', 'i', 'u', 'e', 'o')

  private val letters =
    sentence.toLowerCase.filter(_.ma@@p(_.isLetter).getOrElse(false))

  def wordCount: Int =
    sentence.trim
      .split("\\s+")
      .count(_.nonEmpty)

  def letterCount: Int =
    letters.length

  def vowelCount: Int =
    letters.count(vowels.contains)

  def consonantCount: Int =
    letters.count(c => c.isLetter && !vowels.contains(c))
}

object Main {

  def main(args: Array[String]): Unit = {

    val input = StdIn.readLine()

    val stats = new SentenceStats(input)

    println(
      s"${stats.wordCount} " +
      s"${stats.letterCount} " +
      s"${stats.vowelCount} " +
      s"${stats.consonantCount}"
    )
  }
}
```


#### Short summary: 

empty definition using pc, found symbol in pc: 