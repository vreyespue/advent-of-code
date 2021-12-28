import scala.io.Source

object Puzzle03 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1
    val nrLines =
      io.Source.fromFile("src/main/resources/input03.txt").getLines.size
    val nrBits = 12
    val arrayMeasures = Array.ofDim[Int](nrLines, nrBits)

    val src = Source.fromFile("src/main/resources/input03.txt")
    val iter = src.getLines().map(_.split(" "))

    var countLine = 0
    iter foreach (a => {
      for (i <- 0 to 11) {
        arrayMeasures(countLine)(i) = a(0).toCharArray()(i) - 48
      }
      countLine += 1
    })

    val arraySums = Array.ofDim[Int](nrBits)
    for (i <- 0 to 11) {
      arraySums(i) = arrayMeasures.map(_(i)).sum
      print(arraySums(i) + " ")
    }
    println()

    var gamma_rate: Int = 0
    var epsilon_rate: Int = 0

    for (i <- 0 to 11) {
      if (arraySums(11 - i) >= 500) gamma_rate += 1 * scala.math.pow(2, i).toInt
      else epsilon_rate += 1 * scala.math.pow(2, i).toInt
    }
    println("gamma_rate = " + gamma_rate)
    println("epsilon_rate = " + epsilon_rate)

    println("Result part #1: " + gamma_rate * epsilon_rate)

    src.close()

    // Part #2

  }

  def readFile(filename: String): Seq[String] = {
    val bufferedSource = io.Source.fromFile(filename)
    val lines = (for (line <- bufferedSource.getLines()) yield line).toList
    bufferedSource.close
    lines
  }
}
