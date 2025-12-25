import wmi
import time
import psutil
from pycaw.pycaw import AudioUtilities


def fix_volume(pid):
    # 1. get the process name so we can verify what we are looking at
    try:
        p = psutil.Process(pid)
        process_name = p.name().lower()
        print(f"Checking audio for: {process_name} (PID: {pid})")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        # if process closed quickly or is a restricted system process, skip it
        return

    # 2. check 30 times, every 0.5 seconds (15 seconds total)
    for _ in range(30):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            # Match by PID or by the Process Name (more reliable for games)
            if session.Process and (session.ProcessId == pid or session.Process.name().lower() == process_name):
                volume = session.SimpleAudioVolume
                current_vol = volume.GetMasterVolume()

                # If it's 100% (1.0), drop it to 10% (0.1)
                if current_vol > 0.99:
                    print(f"Success! Lowered {process_name} volume to 10%.")
                    volume.SetMasterVolume(0.1, None)
                    return  # exit the function once fixed

        # If no audio session found yet, wait and try again
        time.sleep(0.5)


def main():
    # Initialize WMI to listen for process creation events
    c = wmi.WMI()
    watcher = c.watch_for(notification_type="Creation", wmi_class="Win32_Process")

    print("Monitoring for new applications... (Keep this window open to see debug prints)")

    while True:
        try:
            # waits until a new app opens
            new_process = watcher()
            process_id = new_process.ProcessId

            # launch the fixer in the background for this specific PID
            fix_volume(process_id)

        except KeyboardInterrupt:
            print("\nStopping monitor...")
            break
        except Exception as e:
            print(f"Error encountered: {e}")
            continue


if __name__ == "__main__":
    main()