import scala.io.StdIn

object Main {
  def main(args: Array[String]): Unit = {

    def parseInput(line: String): Set[String] =
      line.split(",").map(_.trim).toSet

    val data: List[Set[String]] =
      List.fill(4)(StdIn.readLine()).map(parseInput)

    val result: Set[String] =
      data.reduce((a, b) => a.intersect(b))

    val sortedResult: List[String] =
      result.toList.sorted

    println(sortedResult.length)
    sortedResult.foreach(println)
  }
}