import streamlit as st
import paramiko
import os


def send_image_to_inky(image_path, remote_host, remote_user, remote_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_host, username=remote_user, password=remote_password)

    # Use SCP to transfer the file
    sftp = ssh.open_sftp()
    remote_path = '/home/jgu/images/inky_upload.jpg'
    sftp.put(image_path, remote_path)
    sftp.close()

    # Execute the command to update the image on the Inky display
    stdin, stdout, stderr = ssh.exec_command(f'python3 /home/jgu/inky/examples/7color/image.py {remote_path}')
    print(stdout.read().decode())
    print(stderr.read().decode())

    ssh.close()


st.set_page_config(
    page_title="Inky photo uploader",
    page_icon="🏞",
)

st.title("Inky photo uploader 🏞")

uploaded_file = st.file_uploader(label="Choose a file", label_visibility="hidden")


if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    # Save the uploaded file to a temporary location
    image_path = '/Users/jinggu/inky_temp/temp_image.jpg'
    with open(image_path, 'wb') as f:
        f.write(uploaded_file.getvalue())

    # SSH details
    remote_host = 'inky'
    remote_user = 'jgu'
    remote_password = 'jgu0305'

    if st.button('Send to Inky'):
        send_image_to_inky(image_path, remote_host, remote_user, remote_password)
        st.success('Image sent to Inky display!')

    # Clean up the temporary file
    os.remove(image_path)