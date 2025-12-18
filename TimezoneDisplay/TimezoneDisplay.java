import java.time.ZoneId;
import java.time.ZonedDateTime;

public class TimezoneDisplay {
    public static void main(String[] args) {
        try {
            // Retrieve and display the current system timezone
            ZoneId systemZone = ZoneId.systemDefault();
            System.out.println("Current system timezone: " + systemZone);

            // List of timezones to display
            String[] timezones = {"UTC", "America/New_York", "America/Los_Angeles", "GMT", "Asia/Kolkata", "Asia/Tokyo"};

            // Display current time and date for each timezone
            for (String tz : timezones) {
                ZoneId zoneId = ZoneId.of(tz);
                ZonedDateTime now = ZonedDateTime.now(zoneId);
                System.out.println("Current time in " + tz + ": " + now);
            }
        } catch (Exception e) {
            // Handle any exceptions gracefully
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}