/* Rolling Hash mod 2^61-1
 high speed & hash collision resistant
 inspired by @keymoon

remark: 2^61-1 is a Mersenne prime and ~ 2.3*10^18
remark: a*2^61 = a (mod 2^61-1)                     */


// preparation: multiplication without overflow

fun divisionBitUpper(a: Long, n: Int): Long {        // a = p*2^n + q
    return a shr n                                   // p = a // 2^n
}

fun divisionBitLower(a: Long, n: Int): Long {
    return a and ((1.toLong() shl n) - 1)            // q = a and 00..011...1 ("1" * n)
}

// a*b mod 2^61-1 without overflow
fun multiplication(a: Long, b: Long): Long {         // a*b = (ap*2^31 + aq) * (bp*2^31 + bq)
    val ap = divisionBitUpper(a, 31)                 //     = ap*bp * 2^62 + (ap*bq + aq*bp) * 2^31 + aq*bq
    val aq = divisionBitLower(a, 31)                 //     = 2*ap*bp + Cp + Cq * 2^31 + aq*bq
    val bp = divisionBitUpper(b, 31)                 // C = ap*bq + aq*bp ; C = Cp * 2^30 + Cq
    val bq = divisionBitLower(b, 31)
    val cp = divisionBitUpper(ap * bq + aq * bp, 30)
    val cq = divisionBitLower(ap * bq + aq * bp, 30)

    return modMersenne(2*ap*bp + cp + cq*(1.toLong() shl 31) + aq*bq)
}

fun modMersenne(x: Long): Long {
    val mersennePrime = (1.toLong() shl 61) - 1
    var y = x
    while (y < 0) {
        y += mersennePrime
    }
    val dp = divisionBitUpper(y, 61)
    val dq = divisionBitLower(y, 61)
    var d = dp + dq                                  // d = dp*2^61 + dq = dp + dq
    if (d >= mersennePrime) {
        d -= mersennePrime
    }
    return d
}


// define conversion function: Char => Int
fun charToInt(s: String): Int {
    return s.codePointAt(0) - "a".codePointAt(0) + 1
}


// Hash calculation: return hash(s[l ~ r])
fun hashNumber(s: String, base: Int, l: Int, r: Int): Long {
    val n = s.length
    val bData: Array<Long?> = arrayOfNulls(n + 1)
    bData[0] = 1
    val hData: Array<Long?> = arrayOfNulls(n + 1)
    hData[0] = 0
    for (i in 1..n) {
        hData[i] = multiplication(hData[i-1]!!, base.toLong()) + charToInt(s[i-1].toString())
        bData[i] = multiplication(bData[i-1]!!, base.toLong())
    }

    return modMersenne((hData[r]!! - multiplication(hData[l-1]!!, bData[r-l+1]!!)))
}

// Matching
fun main() {
    val (z: Int, q: Int) = readLine()!!.split(" ").map{it.toInt()}
    val s: String = readLine()!!
    val base = 27                                                      
    val n = s.length
    val bData: Array<Long?> = arrayOfNulls(n + 1)
    bData[0] = 1
    val hData: Array<Long?> = arrayOfNulls(n + 1)
    hData[0] = 0
    for (i in 1..n) {
        hData[i] = multiplication(hData[i-1]!!, base.toLong()) + charToInt(s[i-1].toString())
        bData[i] = multiplication(bData[i-1]!!, base.toLong())
    }

    for (k in 1..q) {
        val (l1, r1, l2, r2) = readLine()!!.split(" ").map{it.toInt()}
        val h1 = modMersenne(hData[r1]!! - multiplication(hData[l1 - 1]!!, bData[r1 - l1 + 1]!!))
        val h2 = modMersenne(hData[r2]!! - multiplication(hData[l2 - 1]!!, bData[r2 - l2 + 1]!!))
        if (h1 == h2) {
            println("Yes")
        } else {
            println("No")
        }
    }
}