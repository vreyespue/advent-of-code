import scala.io.Source

object Puzzle02 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1

    val src = Source.fromFile("../aoc2021_input/input02.txt")
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

    // Part #2

    val src2 = Source.fromFile("../aoc2021_input/input02.txt")
    val iter2 = src2.getLines().map(_.split(" "))

    var aim: Int = 0
    var depth: Int = 0
    var horiz_pos: Int = 0
    iter2 foreach (a => {
      if (a(0) == "down") aim += a(1).toInt
      if (a(0) == "up") aim -= a(1).toInt
      if (a(0) == "forward") {
        horiz_pos += a(1).toInt
        depth += aim * a(1).toInt
      }
    })
    println("aim = " + aim)
    println("depth = " + depth)
    println("horiz_pos = " + horiz_pos)

    println("Result part #2: " + depth * horiz_pos)

    src.close()

  }

  def readFile(filename: String): Seq[String] = {
    val bufferedSource = io.Source.fromFile(filename)
    val lines = (for (line <- bufferedSource.getLines()) yield line).toList
    bufferedSource.close
    lines
  }
}
