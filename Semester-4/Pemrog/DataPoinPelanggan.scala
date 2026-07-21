import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

case class Customer(id: Int, poin: Int)
case class Transaksi(id: Int, perubahan: Int)

object DataPoinPelanggan {

  // Pure function: terapkan semua transaksi ke Map poin
  def prosesTransaksi(
    poinMap: Map[Int, Int],
    transaksi: List[Transaksi]
  ): Map[Int, Int] =
    transaksi.foldLeft(poinMap) { (acc, t) =>
      val poinLama = acc.getOrElse(t.id, 0)
      acc.updated(t.id, poinLama + t.perubahan)
    }

  // Pure function: ambil hanya ID yang ada di Set transaksi
  def filterDanUrutkan(
    poinMap: Map[Int, Int],
    idSet: Set[Int]
  ): List[(Int, Int)] =
    poinMap
      .filter { case (id, _) => idSet.contains(id) }
      .toSeq
      .sortBy(_._1)
      .toList

  def main(args: Array[String]): Unit = {
    val br = new BufferedReader(new InputStreamReader(System.in))

    var st = new StringTokenizer(br.readLine())
    val n = st.nextToken().toInt
    val q = st.nextToken().toInt

    // Baca data customer → Map[id, poin]
    val poinAwal: Map[Int, Int] = List.fill(n) {
      st = new StringTokenizer(br.readLine())
      val id   = st.nextToken().toInt
      val poin = st.nextToken().toInt
      (id, poin)
    }.toMap

    // Baca transaksi → List[Transaksi]
    val transaksi: List[Transaksi] = List.fill(q) {
      st = new StringTokenizer(br.readLine())
      val id      = st.nextToken().toInt
      val ubah    = st.nextToken().toInt
      Transaksi(id, ubah)
    }

    // Set berisi ID yang pernah transaksi (otomatis no duplikat)
    val idSet: Set[Int] = transaksi.map(_.id).toSet

    val poinAkhir = prosesTransaksi(poinAwal, transaksi)
    val hasil     = filterDanUrutkan(poinAkhir, idSet)

    println(hasil.size)
    hasil.foreach { case (id, poin) => println(s"$id $poin") }
  }
}