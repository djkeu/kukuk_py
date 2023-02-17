// Suggestion 1
// 1. Replace the Thread.sleep() call in kukuSoundTimes() with a non-blocking delay using coroutines:


private suspend fun delayWithMillis(millis: Long) = withContext(Dispatchers.Default) { delay(millis) }
...
private suspend fun kukuSoundTimes(times: Int) {
    for (i in 1..times) {
        kukuSoundOnce()
        delayWithMillis(1000)
    }
}



// Suggestion 2
/* Avoid using Thread.sleep() in loops or coroutines to avoid blocking the main thread. Instead, use delay() with coroutines to pause for a specified time:
*/

private suspend fun minutelyAlarms() {
    while (true) {
        val getCurrentTime = Calendar.getInstance().time
        val formatter = SimpleDateFormat("mm:ss", Locale.getDefault())
        val currentTime = formatter.format(getCurrentTime)

        for (i in 0..59) {
            val times = if (i == 0) {
                10
            } else if (i < 11) {
                i - 0
            } else if (i < 21) {
                i - 10
            } else if (i < 31) {
                i - 20
            } else if (i < 41) {
                i - 30
            } else if (i < 51) {
                i - 40
            } else {
                i - 50
            }

            val formattedMinute = String.format("%02d", i)
            val minute = "${formattedMinute}:00"

            if (minute == currentTime) {
                kukuSoundTimes(times)
                kukuTextOnce()
            }
        }
        delay(1000)
    }
}




// Suggestion 3: Multiple suggestions
/*
    Avoid using findViewById() repeatedly in the code. Instead, use data binding or ViewBinding to bind views to Kotlin classes.

    You can replace the Calendar.getInstance().time with Date() to get the current date and time.

    Use when statement in place of the long if...else ladder in minutelyAlarms() and hourlyAlarms().

    Add a try-catch block around the MediaPlayer.create() call in kukuSoundOnce() and handle any exceptions that may occur.

    You can move the formatter object to a class-level variable and reuse it in all the methods.

Here is the updated code with the above suggestions implemented:
 */


package nl.djkeu.kukuk

import android.media.MediaPlayer
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.*
import java.text.SimpleDateFormat
import java.util.*


class MainActivity : AppCompatActivity() {

    private val formatter = SimpleDateFormat("mm:ss", Locale.getDefault())

    private var job: Job? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /*
        ToDo: fix UI freeze in minutelyAlarms()
        ToDo: fix UI freezes in hourlyAlarms()
         */

        // Start and stop the alarms
        val kukuScope = MainScope()

        // fun chooseAlarms() {
            // quarterlyAlarms()
            // hourlyAlarms()
            minutelyAlarms()
        }

        suspend fun loopAlarms() {
            while (true) {
                delay(1000)  // Needed to start the UI
                chooseAlarms()
            }
        }

        fun startAlarms() {
            job = kukuScope.launch {
               
