object Main {

    def jumlahGanjil(list: List[Int]): Int = {

        list match {

            case Nil => 0

            case head :: tail =>

                if (head % 2 != 0) {
                    (head * head) + jumlahGanjil(tail)
                }

                else {
                    jumlahGanjil(tail)
                }
        }
    }

    def main(args: Array[String]): Unit = {

        val n = scala.io.StdIn.readInt()

        val angka = scala.io.StdIn.readLine()
            .split(" ")
            .map(_.toInt)
            .toList

        val hasil = jumlahGanjil(angka)

        println(hasil)
    }
}