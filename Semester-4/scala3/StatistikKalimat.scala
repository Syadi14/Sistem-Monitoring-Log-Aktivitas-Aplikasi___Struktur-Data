import scala.io.StdIn

case class TextStats(wordCount: Int, letterCount: Int, vowelCount: Int, consonantCount: Int) {
  override def toString: String = s"$wordCount $letterCount $vowelCount $consonantCount"
}

object TextAnalyzer {
  def analyze(text: String): TextStats = {
    val words = text.split("[^a-zA-Z]+").filter(_.nonEmpty)
    val letters = text.filter(_.isLetter)
    
    val vowels = "aeiouAEIOU".toSet
    val vowelCount = letters.count(vowels.contains)
    val consonantCount = letters.length - vowelCount

    TextStats(words.length, letters.length, vowelCount, consonantCount)
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val input = StdIn.readLine()
    if (input != null) {
      println(TextAnalyzer.analyze(input))
    }
  }
}