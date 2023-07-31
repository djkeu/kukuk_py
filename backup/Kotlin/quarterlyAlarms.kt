    // Quarterly alarms
    @Suppress("unused")
    private fun quarterlyAlarms() {
        val getCurrentTime = Calendar.getInstance().time
        // val getCurrentTime = Date()
        // object formatter is moved to a class level variable, to be used in all alarms
        val formatter = SimpleDateFormat("mm:ss", Locale.getDefault())
        val currentTime = formatter.format(getCurrentTime)

        val quarters = arrayOf( "15:00", "30:00", "45:00" )
        // TEST: val quarters = arrayOf( "05:00", "10:00", "15:00", "20:00", "25:00", "30:00", "35:00", "40:00", "45:00", "50:00", "55:00" )

        if (currentTime in quarters) {
            kukuTextOnce()
            kukuSoundOnce()
        }
    }


