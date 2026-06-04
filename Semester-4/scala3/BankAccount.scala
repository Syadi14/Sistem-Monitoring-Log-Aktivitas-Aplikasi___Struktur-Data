import scala.io.StdIn.readLine

class BankAccount(val accNumber: String, val balance: Double) {
  def credit(amount: Int): BankAccount =
    new BankAccount(accNumber, balance + amount)

  def debit(amount: Int): BankAccount =
    new BankAccount(accNumber, balance - amount)

  def process(amount: Int): BankAccount =
    if (amount >= 0) credit(amount)
    else debit(amount)
}

object BankAccount {
  def buildTransactionMap(data: List[(String, Int)]): Map[String, List[Int]] =
    data.foldLeft(Map[String, List[Int]]()) {
      case (map, (acc, value)) =>
        map.updated(acc, map.getOrElse(acc, List()) :+ value)
    }

  def calculateBalance(acc: String, transactions: List[Int]): BankAccount =
    transactions.foldLeft(new BankAccount(acc, 0.0)) {
      case (account, value) => account.process(value)
    }

  def main(args: Array[String]): Unit = {
    val n = readLine().toInt

    val data = List.fill(n) {
      val input = readLine().split(" ")
      (input(0), input(1).toInt)
    }

    val transactionMap: Map[String, List[Int]] = buildTransactionMap(data)

    val accountOrder = data.map(_._1).distinct

    val result = accountOrder.map { acc =>
      calculateBalance(acc, transactionMap(acc))
    }

    result.foreach { account =>
      println(s"${account.accNumber} : ${account.balance}")
    }
  }
}