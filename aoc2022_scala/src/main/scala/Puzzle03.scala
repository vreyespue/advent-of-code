import scala.io.Source

object Puzzle03 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1
    val nrLines =
      io.Source.fromFile("../input/input03.txt").getLines.size
    val nrBits = 12
    val arrayMeasures = Array.ofDim[Int](nrLines, nrBits)

    val src = Source.fromFile("../input/input03.txt")
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
    println()
    println(
      "arrayMeasures.shape = " + (arrayMeasures.size, arrayMeasures(0).size)
    )
    println()

    var oxygen = arrayMeasures
    for (i <- 0 to 11) {
      if (oxygen.size > 1) {
        if (oxygen.map(_(i)).sum >= (oxygen.map(_(i)).size / 2)) {
          oxygen = oxygen.filter(_(i) == 1)
        } else {
          oxygen = oxygen.filter(_(i) == 0)
        }
        println("oxygen.shape = " + (oxygen.size, oxygen(0).size))
      }
    }
    println()
    println("oxygen = " + oxygen(0).mkString(" "))
    println()

    var co2 = arrayMeasures
    for (i <- 0 to 11) {
      if (co2.size > 1) {
        if (co2.map(_(i)).sum >= (co2.map(_(i)).size / 2)) {
          co2 = co2.filter(_(i) == 0)
        } else {
          co2 = co2.filter(_(i) == 1)
        }
        println("co2.shape = " + (co2.size, co2(0).size))
      }
    }
    println()
    println("co2 = " + co2(0).mkString(" "))
    println()

    var oxygen_rate: Int = 0
    var co2_rate: Int = 0
    for (i <- 0 to 11) {
      oxygen_rate += oxygen(0)(11 - i) * scala.math.pow(2, i).toInt
      co2_rate += co2(0)(11 - i) * scala.math.pow(2, i).toInt

    }
    println("oxygen_rate = " + oxygen_rate)
    println("co2_rate = " + co2_rate)

    println("Result part #2: " + oxygen_rate * co2_rate)

  }

  def readFile(filename: String): Seq[String] = {
    val bufferedSource = io.Source.fromFile(filename)
    val lines = (for (line <- bufferedSource.getLines()) yield line).toList
    bufferedSource.close
    lines
  }
}
