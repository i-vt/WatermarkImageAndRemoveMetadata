# WatermarkImageAndRemoveMetadata
Watermark an Image And Remove image Metadata

## Usage
1. Drop all image files of interest into a directory of choice
2. Modify directory in `processing_dir = "/Users/user/Projects/ImageLaundermat/"` and "br 23 ap" watermark for your own in `original, watermarked = watermark_directory(processing_dir, "br 23 ap", True)` in main.py
3. Run main.py

or

Use  `StandaloneTool.py`
- To clean a directory of image files and remove metadata: ```python main.py --dir /path/to/images --clean```
- To apply a watermark to images in a directory: ```python main.py --dir /path/to/images --watermark "Your Watermark" --watermarking```
- To clean and watermark images in a directory: ```python main.py --dir /path/to/images --watermark "Your Watermark" --clean --watermarking```


## Disclaimer

- General Use: This software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
- Potential Misuse: The software is designed for legitimate purposes only. Any misuse, including but not limited to illegal, unethical, or unauthorized activities, is strictly discouraged and not the intention of the developers.
- User Responsibility: Any person, entity, or organization choosing to use this software bears the full responsibility for its actions while using the software. It is the user's responsibility to ensure that their use of this software complies with local, state, national, and international laws and regulations.
- No Liability: The creators, developers, and distributors of this software are not responsible for any harm or damage caused, directly or indirectly, by the misuse or use of this software.
- Updates and Monitoring: The developers reserve the right to update, modify, or discontinue the software at any time. Users are advised to always use the most recent version of the software. However, even with updates, the developers cannot guarantee that the software is completely secure or free from vulnerabilities.
- Third-Party Software/Links: This software may contain links to third-party sites or utilize third-party software/tools. The developers are not responsible for the content or privacy practices of those sites or software.
- Unauthorized Access: Using "WatermarkImageAndRemoveMetadata" to access, probe, or connect to systems, networks, or data without explicit permission from appropriate parties is strictly discouraged, unethical, and illegal. Unauthorized access to systems, networks, or data breaches various local, national, and international laws, and can result in severe legal consequences. Always obtain the necessary permissions before accessing any systems or data. The developers of "WatermarkImageAndRemoveMetadata" disavow any actions taken by individuals or entities that use this software for unauthorized activities.

By downloading, installing, or using "WatermarkImageAndRemoveMetadata" you acknowledge that you have read, understood, and agreed to abide by this disclaimer. If you do not agree to these terms, do not use the software.
