    // Hourly alarms
    @Suppress("unused", "unused")
    private suspend fun hourlyAlarms() {
        val getCurrentTime = Calendar.getInstance().time
        val formatter = SimpleDateFormat("hh:mm:ss", Locale.getDefault())
        val currentTime = formatter.format(getCurrentTime)

        // ToDo: Use when statement instead of long if..else ladder
        for (i in 1..24) {
            val times = if (i < 13) {
                i - 0
            } else {
                i - 12
            }

            val formattedHour = String.format("%02d", i)
            val hour = "${formattedHour}:00:00"

            if (hour == currentTime) {
                kukuTextOnce()
                // kukuTextTimes(times)
                kukuSoundTimes(times)
            }
        }
    }


