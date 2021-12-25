import scala.io.Source

object Puzzle02 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1

    val src = Source.fromFile("src/main/resources/input02.txt")
    val iter = src.getLines().map(_.split(" "))

    var sumDowns: Int = 0
    var sumUps: Int = 0
    var sumForwards: Int = 0
    iter foreach (a => {
      if (a(0) == "down") sumDowns += a(1).toInt
      if (a(0) == "up") sumUps += a(1).toInt
      if (a(0) == "forward") sumForwards += a(1).toInt
    })
    println("sumDowns = " + sumDowns)
    println("sumUps = " + sumUps)
    println("sumForwards = " + sumForwards)

    println("Result part #1: " + (sumDowns - sumUps) * sumForwards)

    src.close()

  }

  def readFile(filename: String): Seq[String] = {
    val bufferedSource = io.Source.fromFile(filename)
    val lines = (for (line <- bufferedSource.getLines()) yield line).toList
    bufferedSource.close
    lines
  }
}
