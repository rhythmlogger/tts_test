package chat_test;

import java.io.File;

public class Main {
	public static void main(String[] args) {
		String logFolderPath = "C:\\Workspace\\t20230425\\tts_test\\log\\";
		String voiceFolderPath = "C:\\Workspace\\t20230425\\tts_test\\voice\\";
		CustomPlayer player = new CustomPlayer();
		File v = new File(voiceFolderPath);
		File [] files = null;
		while(true) {
			try {
				files = v.listFiles();
				Thread.sleep(1000);
				System.out.println("...sleep3000");
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			if ( files == null) {
				System.out.println("Continue..");
				continue;
			}
			for (int i = 0; i < files.length; i++) {
				System.out.println(files[i].getName());
				String voicePath = voiceFolderPath + files[i].getName();
				player.setPath(voicePath);
				player.play(0);

				try {
					Thread.sleep(1000);
					System.out.println("...sleep2000");
					new File(voicePath).delete();
					new File(logFolderPath + files[i].getName().replace("mp3", "txt")).delete();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
	}
}
