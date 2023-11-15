
// // const body = document.querySelector("body"),
// //     sidebar = body.querySelector(".sidebar"),
// //     rectangleContainer = body.querySelector(".task-bar"),
// //     rectangleContainer1 = body.querySelector(".user-details-bar"),
// //     toggle = body.querySelector(".toggle");
    
// // const defaultSidebarWidth = '180px'; // Change this value based on your default sidebar width


// // function showPopup() {
// //     var popup = document.getElementById("popup");
// //     popup.style.display = "block";
// // }

// // function hidePopup() {
// //     var popup = document.getElementById("popup");
// //     popup.style.display = "none";
// // }

// // toggle.addEventListener("click", () => {
// //     sidebar.classList.toggle("close");

// //     if (sidebar.classList.contains('close')) {
// //         rectangleContainer.style.left = '30px'; // Adjust as needed
// //         rectangleContainer1.style.left = '30px'; // Adjust as needed
// //         rectangleContainer.style.width = `calc(100% - ${defaultSidebarWidth})`;
// //         rectangleContainer1.style.width = `calc(100% - ${defaultSidebarWidth})`;
// //     } else {
// //         rectangleContainer.style.left = defaultSidebarWidth;
// //         rectangleContainer1.style.left = defaultSidebarWidth;
// //         rectangleContainer.style.width = 'calc(100% - 260px)'; // Adjust as needed
// //         rectangleContainer1.style.width = 'calc(100% - 260px)'; // Adjust as needed
// //     }
// // });

// // // Listen for the window scroll event
// // window.addEventListener('scroll', () => {
// //     if (!sidebar.classList.contains('close')) {
// //         // Calculate the new left position based on the current sidebar width
// //         const currentSidebarWidth = sidebar.offsetWidth + 'px';
// //         rectangleContainer.style.left = currentSidebarWidth;
// //         rectangleContainer1.style.left = currentSidebarWidth;
// //     }
// // });



// const body = document.querySelector("body"),
//     sidebar = body.querySelector(".sidebar"),
//     rectangleContainer = body.querySelector(".task-bar"),
//     rectangleContainer1 = body.querySelector(".user-details-bar"),
//     toggle = body.querySelector(".toggle");
    
// const defaultSidebarWidth = '180px'; // Change this value based on your default sidebar width

// function showPopup() {
//     var popup = document.getElementById("popup");
//     popup.style.display = "block";
//     popup.style.top = `${rectangleContainer1.offsetHeight + 0}px`; // Adjust the top position as needed
//     popup.style.left = `${rectangleContainer1.getBoundingClientRect().left}px`; // Align with user-details-bar
// }

// function hidePopup() {
//     var popup = document.getElementById("popup");
//     popup.style.display = "none";
// }

// toggle.addEventListener("click", () => {
//     sidebar.classList.toggle("close");

//     if (sidebar.classList.contains('close')) {
//         rectangleContainer.style.left = '30px'; // Adjust as needed
//         rectangleContainer1.style.left = '30px'; // Adjust as needed
//         rectangleContainer.style.width = `calc(100% - ${defaultSidebarWidth})`;
//         rectangleContainer1.style.width = `calc(100% - ${defaultSidebarWidth})`;
//     } else {
//         rectangleContainer.style.left = defaultSidebarWidth;
//         rectangleContainer1.style.left = defaultSidebarWidth;
//         rectangleContainer.style.width = 'calc(100% - 260px)'; // Adjust as needed
//         rectangleContainer1.style.width = 'calc(100% - 260px)'; // Adjust as needed
//     }
// });

// // Listen for the window scroll event
// window.addEventListener('scroll', () => {
//     if (!sidebar.classList.contains('close')) {
//         // Calculate the new left position based on the current sidebar width
//         const currentSidebarWidth = sidebar.offsetWidth + 'px';
//         rectangleContainer.style.left = currentSidebarWidth;
//         rectangleContainer1.style.left = currentSidebarWidth;
//     }
// });

const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    rectangleContainer = body.querySelector(".task-bar"),
    rectangleContainer1 = body.querySelector(".user-details-bar"),
    toggle = body.querySelector(".toggle");
const defaultSidebarWidth = '180px'; // Change this value based on your default sidebar width

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");

    if (sidebar.classList.contains('close')) {
        rectangleContainer.style.left = '30px'; // Adjust as needed
        rectangleContainer1.style.left = '30px'; // Adjust as needed
        rectangleContainer.style.width = `calc(100% - ${defaultSidebarWidth})`;
        rectangleContainer1.style.width = `calc(100% - ${defaultSidebarWidth})`;
    } else {
        rectangleContainer.style.left = defaultSidebarWidth;
        rectangleContainer1.style.left = defaultSidebarWidth;
        // rectangleContainer.style.width = 'calc(100% - 260px)'; // Adjust as needed
        rectangleContainer.style.width = 'calc(100% - 500px)';
        rectangleContainer1.style.width = 'calc(100% - 260px)'; // Adjust as needed
    }
});

// Listen for the window scroll event
window.addEventListener('scroll', () => {
    if (!sidebar.classList.contains('close')) {
        // Calculate the new left position based on the current sidebar width
        const currentSidebarWidth = sidebar.offsetWidth + 'px';
        rectangleContainer.style.left = currentSidebarWidth;
        rectangleContainer1.style.left = currentSidebarWidth;
    }
});


function showPopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "block";

    var addButton = document.querySelector(".add_task"); // Replace with the selector for your button
    var buttonRect = addButton.getBoundingClientRect();

    // Calculate the desired top and left positions for the popup
    var desiredTop = buttonRect.bottom + window.scrollY; // Position below the button
    var desiredLeft = buttonRect.left;

    // Set the top and left positions for the popup
    popup.style.top = `${desiredNear}px`;
    popup.style.left = `${desiredLeft}px`;

    // Set the z-index to a high value to make the popup appear in front
    popup.style.zIndex = "1000"; // You can adjust this value as needed

    // Remove background color and box shadow
    popup.style.backgroundColor = "transparent";
    popup.style.boxShadow = "none";
}

function hidePopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "none";
}

