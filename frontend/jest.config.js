module.exports = {
    testEnvironment: "jsdom",
    transform: {
        "^.+\\.vue$": "@vue/vue3-jest",
        "^.+\\.js$": "babel-jest", // Corrected the backslash before '.js'
    },
    testRegex: "(/__tests__/.*|(\\.|/)(test|spec))\\.(js|ts)$",
    moduleFileExtensions: ["vue", "js"],
    moduleNameMapper: {
        "^@/(.*)$": "<rootDir>/src/$1",
        '\\.(jpg|jpeg|png|gif|webp|svg)$': '<rootDir>/__mocks__/fileMock.js', // Static asset mocks
    },
    coveragePathIgnorePatterns: ["/node_modules/", "/tests/"],
    coverageReporters: ["text", "json-summary"],
    testEnvironmentOptions: {
        customExportConditions: ["node", "node-addons"],
    },
    // Add any other configurations here as necessary
}


