object Puzzle01 {
  def main(args: Array[String]) = {
    println("Hello, world")
    println(System.getProperty("user.dir"))

    // Part #1

    val myListString = readFile("../input/input01.txt")
    println("myListString = " + myListString)

    val myListLong = myListString.map(_.toLong)
    println("myListLong = " + myListLong)

    //Smaller list for testing purposes
    //val myListLongShort = myListLong.take(5)
    //println("myListLongShort = " + myListLongShort)

    val myListDiff =
      myListLong.sliding(2).map { case Seq(x, y) => y - x }.toList
    println("myListDiff = " + myListDiff)

    val myListIncreased = myListDiff.filter(_ > 0)
    println("myListIncreased = " + myListIncreased)

    val myListIncreasedLength = myListIncreased.length
    println("Result part #1: " + myListIncreasedLength)

    //Alternative solution using foldLeft
    //var myCount: Long = 0
    //val myListIncFold = myListLong.foldLeft(Long.MaxValue) { (z, i) =>
    //  {
    //    //println(z + " " + i)
    //    if (z < i) myCount = myCount + 1
    //    i
    //  }
    //}
    //println(myCount)

    // Part #2

    val myListSliding3 = myListLong.sliding(3).toList
    println("myListSliding3 = " + myListSliding3)

    val myListSliding3Sum = myListSliding3.map(_.sum)
    //Alternative solution using case
    //val myListSliding3Sum = myListSliding3.map { case Seq(x, y, z) =>
    //  x + y + z
    //}
    println("myListSliding3Sum = " + myListSliding3Sum)

    val myListSliding3Diff =
      myListSliding3Sum.sliding(2).map { case Seq(x, y) => y - x }.toList
    println("myListSliding3Diff = " + myListSliding3Diff)

    val myListSliding3Increased = myListSliding3Diff.filter(_ > 0)
    println("myListSliding3Increased = " + myListSliding3Increased)

    val myListSliding3IncreasedLength = myListSliding3Increased.length
    println("Result part #2: " + myListSliding3IncreasedLength)

  }

  def readFile(filename: String): Seq[String] = {
    val bufferedSource = io.Source.fromFile(filename)
    val lines = (for (line <- bufferedSource.getLines()) yield line).toList
    bufferedSource.close
    lines
  }
}
