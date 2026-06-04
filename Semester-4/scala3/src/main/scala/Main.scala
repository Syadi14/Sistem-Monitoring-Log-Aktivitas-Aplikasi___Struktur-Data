import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {

    println("Hello, World!")

    print("What is your name? ")
    val name = readLine()

    println("Nice to meet you, " + name + "!")
  }
}