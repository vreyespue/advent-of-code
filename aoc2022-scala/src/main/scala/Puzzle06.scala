object Puzzle06 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1

    val myString = readFile("../aoc2022-input/input06.txt").mkString("")
    println("myString = " + myString)

    val string1 = "abcdefg"
    println("string1 = " + string1)
    val string2 = string1.slice(0, 4)
    println("string2 = " + string2)
    val count = string2.toSet.size
    println("count = " + count)

    val startPacket = findStartPacket(myString, 0)
    println("Part #1 startPacket = " + startPacket)

    val startMessage = findStartMessage(myString, 0)
    println("Part #2 startMessage = " + startMessage)

  }

  def findStartPacket(input: String, i: Int): Int =
    if (input.slice(i, i + 4).toSet.size == 4) then i +4
    else findStartPacket(input, i + 1)

  def findStartMessage(input: String, i: Int): Int =
    if (input.slice(i, i + 14).toSet.size == 14) then i +14
    else findStartMessage(input, i + 1)

  def readFile(filename: String): Seq[String] = {
    val bufferedSource = io.Source.fromFile(filename)
    val lines = (for (line <- bufferedSource.getLines()) yield line).toList
    bufferedSource.close
    lines
  }
}
