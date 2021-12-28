import scala.io.Source

object Puzzle03 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1

    val src = Source.fromFile("src/main/resources/input03.txt")
    val iter = src.getLines().map(_.split(" "))

    iter foreach (a => {
      println(a(0).toCharArray()(0))
    })
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
