// Test for the hello function
function testHello() {
    // Call the hello function
    hello();

    // Check if an alert with the message "Hello, World!" was shown
    // You can use a testing library like Jest to make assertions
    // Here's an example using Jest:
    expect(window.alert).toHaveBeenCalledWith("Hello, World!");
}

// Run the test
testHello();