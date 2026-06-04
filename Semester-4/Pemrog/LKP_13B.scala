object Main {
    def main(args: Array[String]): Unit = {

        val first = scala.io.StdIn.readLine().split(" ")

        val n = first(0).toInt
        val batas = first(1).toInt

        var mahasiswa = Map[String, Int]()

        for (i <- 0 until n) {

            val data = scala.io.StdIn.readLine().split(" ")

            val nama = data(0)
            val nilai = data(1).toInt

            mahasiswa += (nama -> nilai)
        }

        val lulus = mahasiswa.filter { case (nama, nilai) =>
            nilai >= batas
        }

        val urut = lulus.toSeq.sortBy { case (nama, nilai) =>
            nama
        }

        println(urut.size)

        for ((nama, nilai) <- urut) {
            println(s"$nama $nilai")
        }
    }
}