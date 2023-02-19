    // Minutely alarms
    @Suppress("unused")
    private suspend fun minutelyAlarms() {
        while (true) {  // TODO: while loop needed?
            val getCurrentTime = Calendar.getInstance().time
            val formatter = SimpleDateFormat("mm:ss", Locale.getDefault())
            val currentTime = formatter.format(getCurrentTime)

            // TODO: Use when statement instead of long if..else ladder
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
                    kukuTextOnce()
                    // kukuTextTimes(times)
                    kukuSoundTimes(times)
                }
            }
            delay(1000)
        }
    }
