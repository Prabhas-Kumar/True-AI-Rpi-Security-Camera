# What is this?

This is the explaination of my programs & guide to a bonus way of doing the se-up.

## Bonus-way

First of all make sure the camera interface is enabled in the Raspberry Pi Configuration menu. Click the Pi icon in the top left corner of the screen, select Preferences -->  Raspberry Pi Configuration, and go to the Interfaces tab and verify Camera is set to Enabled. If it isn't, enable it now, and reboot the Raspberry Pi.

After insuring it is enabled open the terminal either via a terminal icon above or via a shortkut key combitation [Ctrl + Alt + T] then issue:

```

git clone https://github.com/Prabhas-Kumar/True-AI-Rpi-Security-Camera.git
mv True-AI-Rpi-Security-Camerarue-AI-Rpi-Security-Camera tflite1
cd tflite1
sudo bash setup_of_Epi_for_Thlite.sh
```

This downloads about 400MB worth of installation files, so it will take a while. Go grab a cup of coffee while it's working! If you'd like to see everything that gets installed, simply open get_pi_dependencies.sh to view the list of packages.

### You'll need to issue the source tflite1-env/bin/activate command from inside the /home/pi/tflite1 directory to reactivate the environment every time you open a new terminal window. You can tell when the environment is active by checking if (tflite1-env) appears before the path in your command prompt, as shown in the screenshot below.

After it is been downloaded issue this:
```

sudo bash setup_of_Rpi_for_Thlite_part2.sh
```

After it's been completed issue this to test it:
```

ython3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model
```

If your model folder has a different name than "Sample_TFLite_model", use that name instead. For example, I would use --modeldir=BirdSquirrelRaccoon_TFLite_model to run my custom bird, squirrel, and raccoon detection model.
