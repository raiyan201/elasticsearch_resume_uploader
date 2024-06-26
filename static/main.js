// const fileUploader = document.getElementById('uploadfiles');
// const progressArea = document.getElementById('progress-area');
// const reader = new FileReader();
// /*input*/
// fileUploader.addEventListener('change', (event) => {

//     // document.querySelectorAll('.progress-wrapper').forEach(wrapper => wrapper.remove());
//     const files = event.target.files;

//     for (let i = 0; i < files.length; i++) {
//         const file = files[i];
//         const reader = new FileReader();
        
//         createProgressBar(file);    

//         reader.readAsDataURL(file);
//         reader.addEventListener('progress', (event) => {
//             updateProgressBar(event, file);
//         });
//     }
// });


// function createProgressBar(file) {

//     // const existingProgressBar = document.querySelector(`progress[data-file="${file.name}"]`);
    
//     // if (existingProgressBar && existingProgressBar.closest('.progress-wrapper')) {
//     //     existingProgressBar.closest('.progress-wrapper').remove();
//     // }

//     const progressBarWrapper = document.createElement('div');
//     const progressBarLabel = document.createElement('label');
//     const progressBar = document.createElement('progress');
//     const progressBarMessage = document.createElement('span'); 
//     progressBarWrapper.classList.add('progress-wrapper');
//     progressBar.setAttribute('data-file', file.name);
//     progressBar.setAttribute('max', 100);
//     progressBarLabel.innerText = file.name;
//     progressBarWrapper.appendChild(progressBarLabel);
//     progressBarWrapper.appendChild(progressBar);
//     progressBarWrapper.appendChild(progressBarMessage); 
//     progressArea.appendChild(progressBarWrapper);
// }


// function updateProgressBar(event, file) {
//     if (event.loaded && event.total) {
//         const percent = (event.loaded / event.total) * 100;
//         const progressBar = document.querySelector(`progress[data-file="${file.name}"]`);
        
//         if (progressBar) {
//             progressBar.value = percent;
//             const labelElem = progressBar.previousSibling;
//             const feedbackElem = progressBar.nextSibling;
            
//             if (labelElem) {
//                 labelElem.innerText = file.name + " " + Math.round(percent) + '%';
//             }

//             if (percent === 100 && feedbackElem) {
//                 feedbackElem.innerText = `File ${file.name} has been uploaded successfully.`;
                
//                 setTimeout(() => {
//                     const wrapperElem = progressBar.closest('.progress-wrapper');
//                     if (wrapperElem) {
//                         wrapperElem.style.display = 'none'; 
//                     }
//                 }, 1000);
//             }
//         }
//     }
// }

