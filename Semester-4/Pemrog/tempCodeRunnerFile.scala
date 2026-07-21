import scala.io.StdIn.readLine

case class Transaksi(idProduk: Int, jumlahBarang: Int, hargaSatuan: Int)

object PenjualanBarang {
    def pendapatan(t: Transaksi): Long = t.jumlahBarang.toLong * t.hargaSatuan
    def hitungHasil(
    transaksi: List[Transaksi],
    minJumlah: Int,
    batasPendapatan: Long
    ): List[(Int, Long)] = {
        transaksi
            .filter(t => t.jumlahBarang >= minJumlah)
            .map(t => (t.idProduk, pendapatan(t)))
            .groupBy(_._1)
            .map{ case (k, list) => (k, list.map(_._2).sum) }
            .filter {case (_,total) => total >= batasPendapatan}
            .toSeq
            .sortBy(_._1)
            .toList
    }

    def main(args: Array[String]): Unit = {
        val Array(n, minJumlah, batasPendapatan) = readLine().trim.split(" ").map(_.toLong)
        val transaksi: List[Transaksi] = List.fill(n.toInt){
            val Array(id, jumlah, harga) = readLine().trim.split(" ").map(_.toInt)
            Transaksi(id, jumlah, harga)
        }
        val hasil = hitungHasil(transaksi, minJumlah.toInt, batasPendapatan)
        
        if (hasil.isEmpty){
            println(0)
        } else {
            println(hasil.size)
            hasil.foreach{case (id, total) => println(s"$id $total")}
        }
    }
}