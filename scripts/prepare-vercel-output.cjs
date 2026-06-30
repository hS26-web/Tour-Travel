const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const srcDir = path.join(root, "src");
const packagesDir = path.join(root, "packages");
const distDir = path.join(root, "dist");

function copyDir(from, to) {
  fs.cpSync(from, to, { recursive: true });
}

fs.rmSync(distDir, { recursive: true, force: true });
fs.mkdirSync(distDir, { recursive: true });

copyDir(srcDir, distDir);
copyDir(packagesDir, path.join(distDir, "packages"));

const packageOutputDir = path.join(distDir, "packages");
for (const file of fs.readdirSync(packageOutputDir)) {
  if (!file.endsWith(".html")) continue;

  const packagePath = path.join(packageOutputDir, file);
  let packageHtml = fs.readFileSync(packagePath, "utf8");
  packageHtml = packageHtml
    .replaceAll("../src/assets/", "../assets/")
    .replaceAll("../src/index.html", "../index.html")
    .replaceAll("../src/about.html", "../about.html")
    .replaceAll("../src/destination.html", "../destination.html")
    .replaceAll("../src/contact.html", "../contact.html")
    .replaceAll("../src/terms&condition.html", "../terms&condition.html")
    .replaceAll("../src/privacypolicy.html", "../privacypolicy.html");
  fs.writeFileSync(packagePath, packageHtml);
}
