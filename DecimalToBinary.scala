def toBinary(n:Int, bin: List[Int] = List.empty[Int]): String = {
  if(n/2 == 1) (1:: (n % 2) :: bin).mkString(" ")
  else {
    val r = n % 2
    val q = n / 2
    toBinary(q, r::bin)
  }
}