// const body = document.querySelector("body"),
//     sidebar = body.querySelector(".sidebar"),
//     rectangleContainer = body.querySelector(".task-bar"),
//     rectangleContainer1 = body.querySelector(".user-details-bar"),
//     toggle = body.querySelector(".toggle"),
//     totalUserBox = document.querySelector('.totalUser .box'),
//     technicianDiv = body.querySelector('.totalTechnician .box2'),
//     organizerDiv = body.querySelector('.totalOrganizer .box3');

// const defaultTotalUserLeft = '280px';
// const defaultTechnicianMargin = '8px';
// const defaultRectangleLeft = '260px';
// const defaultRectangle1Left = '260px';

// toggle.addEventListener("click", () => {
//     sidebar.classList.toggle("close");

//     if (sidebar.classList.contains('close')) {
//         totalUserBox.style.left = '80px';
//         technicianDiv.style.marginLeft = defaultTechnicianMargin;
//         rectangleContainer.style.left = '80px';
//         rectangleContainer1.style.left = '80px';
//         rectangleContainer.style.width = 'calc(100% - 80px)';
//         rectangleContainer1.style.width = 'calc(100% - 80px)';
//     } else {
//         totalUserBox.style.left = defaultTotalUserLeft;
//         technicianDiv.style.marginLeft = '90px';
//         rectangleContainer.style.left = defaultRectangleLeft;
//         rectangleContainer1.style.left = defaultRectangleLeft;
//         rectangleContainer.style.width = 'calc(100% - 260px)';
//         rectangleContainer1.style.width = 'calc(100% - 260px)';
//     }
// });

// // Adjust the rectangle's position and width when the page loads
// window.addEventListener("load", () => {
//     if (sidebar.classList.contains('close')) {
//         rectangleContainer.style.left = '80px';
//         rectangleContainer.style.width = 'calc(100% - 80px)';
//         rectangleContainer1.style.left = '80px';
//         rectangleContainer1.style.width = 'calc(100% - 80px)';
//     }
// });

// // Listen for the window scroll event
// window.addEventListener('scroll', () => {
//     if (sidebar.classList.contains('close')) {
//         totalUserBox.style.display = 'none';
//         rectangleContainer.style.display = 'none';
//         rectangleContainer1.style.display = 'none';
//     } else {
//         totalUserBox.style.display = 'block';
//         rectangleContainer.style.display = 'block';
//         rectangleContainer1.style.display = 'block';
//     }
// });