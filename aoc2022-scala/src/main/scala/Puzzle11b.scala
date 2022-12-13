import scala.util.control.Breaks._

object Puzzle11b {
  trait Monkey:
    var name: String
    var items: Array[Long]
    var nrInspections: Long = 0

    def operation(old: Long): Long

    def test(value: Long): Int

  def main(args: Array[String]) =
    println("Hello, world")
    println(System.getProperty("user.dir"))

    var monkey0 = new Monkey() {
      var name = "monkey0"
      var items = Array(72, 97)

      def operation(old: Long): Long =
        old * 13

      def test(value: Long): Int =
        if (value % 19 == 0) 5 else 6
    }

    var monkey1 = new Monkey() {
      var name = "monkey1"
      var items = Array(55, 70, 90, 74, 95)

      def operation(old: Long): Long =
        old * old

      def test(value: Long): Int =
        if (value % 7 == 0) 5 else 0
    }

    var monkey2 = new Monkey() {
      var name = "monkey2"
      var items = Array(74, 97, 66, 57)

      def operation(old: Long): Long =
        old + 6

      def test(value: Long): Int =
        if (value % 17 == 0) 1 else 0
    }

    var monkey3 = new Monkey() {
      var name = "monkey3"
      var items = Array(86, 54, 53)

      def operation(old: Long): Long =
        old + 2

      def test(value: Long): Int =
        if (value % 13 == 0) 1 else 2
    }

    var monkey4 = new Monkey() {
      var name = "monkey4"
      var items = Array(50, 65, 78, 50, 62, 99)

      def operation(old: Long): Long =
        old + 3

      def test(value: Long): Int =
        if (value % 11 == 0) 3 else 7
    }

    var monkey5 = new Monkey() {
      var name = "monkey5"
      var items = Array(90)

      def operation(old: Long): Long =
        old + 4

      def test(value: Long): Int =
        if (value % 2 == 0) 4 else 6
    }

    var monkey6 = new Monkey() {
      var name = "monkey6"
      var items = Array(88, 92, 63, 94, 96, 82, 53, 53)

      def operation(old: Long): Long =
        old + 8

      def test(value: Long): Int =
        if (value % 5 == 0) 4 else 7
    }

    var monkey7 = new Monkey() {
      var name = "monkey7"
      var items = Array(70, 60, 71, 69, 77, 70, 98)

      def operation(old: Long): Long =
        old * 7

      def test(value: Long): Int =
        if (value % 3 == 0) 2 else 3
    }

    var arrayMonkeys = Array(
      monkey0,
      monkey1,
      monkey2,
      monkey3,
      monkey4,
      monkey5,
      monkey6,
      monkey7
    )

    for (round <- 1 to 10000)
      println("Round " + round)
//      println("countAllItems: " + countAllItems(arrayMonkeys))
//      println()

      for (monkey <- arrayMonkeys)
//        println("monkey.name = " + monkey.name)
//        println("monkey.items = " + monkey.items.mkString(", "))
//        println("countAllItems: " + countAllItems(arrayMonkeys))
        // monkey.operation()
        // monkey.testVal()

        for (item <- monkey.items)
          monkey.nrInspections += 1
//          println("item = " + item)
          var newValue = monkey.operation(item)
//          println("newValue = " + newValue)
          // newValue = newValue / 3
          newValue = newValue % (19 * 7 * 17 * 13 * 11 * 2 * 5 * 3)
//          println("newValue = " + newValue)
          var nextMonkey = monkey.test(newValue)
//          println("nextMonkey = " + nextMonkey)
//          println(
//            "arrayMonkeys(nextMonkey).items = " + arrayMonkeys(
//              nextMonkey
//            ).items
//              .mkString(", ")
//          )
          arrayMonkeys(nextMonkey).items =
            arrayMonkeys(nextMonkey).items :+ newValue
//          println(
//            "arrayMonkeys(nextMonkey).items = " + arrayMonkeys(
//              nextMonkey
//            ).items
//              .mkString(", ")
//          )

        monkey.items = Array()
//        println()
//        println("countAllItems: " + countAllItems(arrayMonkeys))
//        println()

//      println()
//      println()

    println("Final")
    for (monkey <- arrayMonkeys)
      println("monkey.name = " + monkey.name)
      // println("monkey.items = " + monkey.items.mkString(", "))
      println("monkey.nrInspections = " + monkey.nrInspections)

    def countAllItems(arrayMonkeys: Array[Monkey]): Long =
      var count = 0
      for (monkey <- arrayMonkeys)
        count += monkey.items.length
      count
}
