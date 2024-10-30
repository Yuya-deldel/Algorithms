/* Rolling Hash mod 2^61-1
 high speed & hash collision resistant
 inspired by @keymoon */

// preparation: multiplication without overflow

val bit30m1: Long = 1073741823
val bit31: Long = 2147483648
val bit31m1: Long = 2147483647
val bit61: Long = 2305843009213693952
val mersennePrime :Long = 2305843009213693951     // bit61 - 1 = 2^61 - 1

fun modMersenne(x: Long): Long {
    var y = x
    if (y < 0) {
        while (y < 0) {
            y += mersennePrime
        }
        return y
    } else {
        val dp = y shr 61
        val dq = y and mersennePrime
        var d = dp + dq                                  
        if (d >= mersennePrime) {
            d -= mersennePrime
        }
        return d
    }
}

fun multiplication(a: Long, b: Long): Long {        
    val ap = a shr 31                 
    val aq = a and bit31m1
    val bp = b shr 31             
    val bq = b and bit31m1
    val c = ap * bq + aq * bp
    val cp = c shr 30
    val cq = c and bit30m1

    return modMersenne(2*ap*bp + cp + cq*bit31 + aq*bq)
}


// define conversion function: Char => Int
fun charToInt(s: String): Int {
    return s.codePointAt(0) - "a".codePointAt(0) + 1
}

// Hash calculation: return hash(s[l ~ r])
fun hashNumber(s: String, base: Long, l: Int, r: Int): Long {
    val n = s.length
    val bData: Array<Long?> = arrayOfNulls(n + 1)
    bData[0] = 1
    val hData: Array<Long?> = arrayOfNulls(n + 1)
    hData[0] = 0
    for (i in 1..n) {
        hData[i] = multiplication(hData[i-1]!!, base) + charToInt(s[i-1].toString())
        bData[i] = multiplication(bData[i-1]!!, base)
    }

    return modMersenne((hData[r]!! - multiplication(hData[l-1]!!, bData[r-l+1]!!)))
}

// Matching : change Inputs and base if necessary
fun main() {
    val (z: Int, q: Int) = readLine()!!.split(" ").map{it.toInt()}
    val s: String = readLine()!!
    val primes: List<Long> = listOf(29, 31, 37, 41, 43, 47, 53, 59, 61, 67)
    val base: Long = primes.random()
    val n = s.length
    val bData: Array<Long?> = arrayOfNulls(n + 1)
    bData[0] = 1
    val hData: Array<Long?> = arrayOfNulls(n + 1)
    hData[0] = 0
    for (i in 1..n) {
        hData[i] = multiplication(hData[i-1]!!, base) + charToInt(s[i-1].toString())
        bData[i] = multiplication(bData[i-1]!!, base)
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