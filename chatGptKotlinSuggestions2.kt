/*
There are a few ways that the Kotlin code can be improved:

    Avoid blocking the main thread

The minutelyAlarms and hourlyAlarms functions contain loops that can cause the app to freeze if they are executed on the main thread. To avoid this, these functions can be executed on a background thread using coroutines.

    Use better naming conventions

Variable and function names should be descriptive and use consistent naming conventions. For example, it would be clearer to rename chooseAlarms() to something like startSelectedAlarms(). It's also a good practice to use camelCase for function and variable names and PascalCase for class names.

    Remove unused code

The quarterlyAlarms() function is currently marked as @Suppress("unused"), indicating that it is not used in the current version of the code. Removing this function will make the code easier to read and maintain.

    Refactor repetitive code

The kukuTextOnce() and kukuSoundOnce() functions contain similar logic. To avoid repetition, they can be combined into a single function that takes a parameter indicating whether to play the sound or show the text.

    Use sealed classes for constants

The quarters array in the quarterlyAlarms() function contains a fixed set of values. To make this more explicit, it can be defined as a sealed class with a fixed set of subclasses.

Here is an example of how the code can be improved:
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
    private val kukuScope = MainScope()
    private var job: Job? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        startSelectedAlarms()
    }

    private fun startSelectedAlarms() {
        stopAlarms()
        job = kukuScope.launch {
            loopAlarms()
        }
    }

    private fun stopAlarms() {
        job?.cancel()
        job = null
    }

    private suspend fun loopAlarms() {
        while (true) {
            delay(1000)
            minutelyAlarms()
            hourlyAlarms()
        }
    }

    private fun kukuAlert(playSound: Boolean, showText: Boolean) {
        if (playSound) {
            val resourceId = resources.getIdentifier("keukuk", "raw", packageName)
            val kukuPlayer = MediaPlayer.create(this, resourceId)
            kukuPlayer.start()
        }

        if (showText) {
            val kukuToast = Toast.makeText(applicationContext,
                getString(R.string.kukukTextView),
                Toast.LENGTH_LONG)

            kukuToast.show()
        }
    }

    private sealed class Quarter(val time: String) {
        object Quarter15 : Quarter("15:00")
        object Quarter30 : Quarter("30:00")
        object Quarter45 : Quarter("45:00")
    }

    private suspend fun quarterlyAlarms() {
        val getCurrentTime = Calendar.getInstance().time
        val formatter = SimpleDateFormat("mm:ss", Locale.getDefault())
        val currentTime = formatter.format(getCurrentTime)

        when (currentTime) {
            Quarter.Quarter15.time -> kukuAlert(true, true)
            Quarter.Quarter30.time -> kukuAlert(true, true)
            Quarter.Quarter45.time -> kukuAlert(true, true)
        }
    }

    private suspend fun hourlyAlarms() {
        val getCurrentTime = Calendar.getInstance().time
        val formatter = SimpleDateFormat("hh:mm:ss", Locale


