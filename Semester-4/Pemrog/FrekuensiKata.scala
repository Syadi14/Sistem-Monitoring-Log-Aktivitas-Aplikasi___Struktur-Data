import java.io.BufferedReader
import java.io.InputStreamReader

object FrekuensiKata {

  def prosesKata(baris: List[String]): List[(String, Int)] =
    baris
      .flatMap(_.split("[^a-zA-Z]+"))   // pecah tiap baris by non-huruf
      .filter(_.nonEmpty)               // buang string kosong
      .map(_.toLowerCase)               // samakan huruf besar/kecil
      .groupBy(identity)                // kelompokkan kata yang sama
      .view.mapValues(_.size)           // hitung frekuensi tiap kata
      .toSeq
      .sortBy(_._1)                     // urutkan alfabetis
      .toList

  def main(args: Array[String]): Unit = {
    val br = new BufferedReader(new InputStreamReader(System.in))
    val n = br.readLine().trim.toInt

    val baris: List[String] = List.fill(n)(br.readLine())

    val hasil = prosesKata(baris)
    hasil.foreach { case (kata, freq) => println(s"$kata $freq") }
  }
}