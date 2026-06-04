import scala.io.StdIn

object AnalisisNilaiMahasiswa {
  case class Mahasiswa(nama: String, nilai: Int, urutan: Int)
  def main(args: Array[String]): Unit = {
    val n = StdIn.readLine().trim.toInt

    val dtMahasiswa = (0 until n).toList.map { i =>
      val baris = StdIn.readLine().split(",")
      Mahasiswa(baris(0).trim, baris(1).trim.toInt, i)
    }

    val topFive = dtMahasiswa
      .filter(_.nilai >= 75)
      .sortBy(m => (m.nilai, m.urutan))
      .reverse
      .take(5)

    topFive.foreach(m => println(s"${m.nama} : ${m.nilai}"))
  }
}