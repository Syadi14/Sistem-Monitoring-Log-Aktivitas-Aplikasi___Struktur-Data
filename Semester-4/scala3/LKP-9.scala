object Main {

  def normalizeScore(x: Int): Int = {
    if (x < 0) 0
    else if (x > 100) 100
    else x
  }

  def bonusScore(x: Int): Int = {
    val result = x + 5
    if (result > 100) 100 else result
  }

  def transformScores(scores: List[Int], f: Int => Int): List[Int] = {
    scores.map(f)
  }

  def main(args: Array[String]): Unit = {
    val n = scala.io.StdIn.readInt()
    val scores = scala.io.StdIn.readLine().trim.split("\\s+").map(_.toInt).toList
    val normalized = transformScores(scores, normalizeScore)
    val finalScores = transformScores(normalized, bonusScore)
    val lulus = finalScores.filter(x => x >= 60)
    val total = finalScores.foldLeft(0)(_ + _)
    val rata = total.toDouble / finalScores.length
    val maksimum = finalScores.foldLeft(0)((acc, x) =>
      if (x > acc) x else acc
    )

    println(finalScores)
    println(lulus)
    println(lulus.length)
    println(total)
    println(rata)
    println(maksimum)
  }
}